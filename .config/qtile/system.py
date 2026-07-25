"""
FreeBSD system information helpers for Qtile.

These functions provide text for Qtile GenPollText widgets.

They intentionally use FreeBSD-native commands such as:
- sysctl
- ifconfig
- mixer
- acpiconf
- netstat

Every function safely returns a fallback value when hardware,
a service, or a command is unavailable.
"""

from __future__ import annotations

import re
import subprocess
import time
from pathlib import Path


# ==========================================================
# GENERAL HELPERS
# ==========================================================

WIFI_INTERFACE = "wlan0"
NETWORK_INTERFACE = "wlan0"

_net_previous_time: float | None = None
_net_previous_received: int | None = None
_net_previous_sent: int | None = None


def run_command(command: list[str]) -> str:
    """
    Run a command without opening a shell.

    Returns an empty string when the command fails.
    """

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=2,
        )

        if result.returncode != 0:
            return ""

        return result.stdout.strip()

    except (
        FileNotFoundError,
        PermissionError,
        subprocess.SubprocessError,
        OSError,
    ):
        return ""


def read_sysctl(name: str) -> str:
    """
    Read a FreeBSD sysctl value.
    """

    return run_command(["sysctl", "-n", name])


def format_rate(bytes_per_second: float) -> str:
    """
    Convert bytes per second into a compact readable value.
    """

    if bytes_per_second < 0:
        bytes_per_second = 0

    units = ("B", "K", "M", "G", "T")
    value = float(bytes_per_second)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{value:.0f}{unit}/s"

            return f"{value:.1f}{unit}/s"

        value /= 1024

    return "0B/s"


# ==========================================================
# BATTERY
# ==========================================================

def get_battery_status() -> str:
    """
    Return battery percentage and charging state.
    """

    life_text = read_sysctl("hw.acpi.battery.life")
    state_text = read_sysctl("hw.acpi.battery.state")
    time_text = read_sysctl("hw.acpi.battery.time")

    try:
        percentage = int(life_text)
    except ValueError:
        return "󰂑 N/A"

    try:
        state = int(state_text)
    except ValueError:
        state = -1

    if state == 2:
        icon = "󰂄"
    elif percentage >= 90:
        icon = "󰁹"
    elif percentage >= 80:
        icon = "󰂂"
    elif percentage >= 70:
        icon = "󰂁"
    elif percentage >= 60:
        icon = "󰂀"
    elif percentage >= 50:
        icon = "󰁿"
    elif percentage >= 40:
        icon = "󰁾"
    elif percentage >= 30:
        icon = "󰁽"
    elif percentage >= 20:
        icon = "󰁼"
    elif percentage >= 10:
        icon = "󰁻"
    else:
        icon = "󰂎"

    remaining = ""

    try:
        minutes = int(time_text)

        if minutes > 0:
            hours, minutes = divmod(minutes, 60)
            remaining = f" {hours}:{minutes:02d}"

    except ValueError:
        pass

    return f"{icon} {percentage}%{remaining}"


# ==========================================================
# WI-FI
# ==========================================================

def get_wifi_status() -> str:
    """
    Return the current wireless SSID.
    """

    output = run_command(["ifconfig", WIFI_INTERFACE])

    if not output:
        return "󰖪 Offline"

    ssid_match = re.search(r"\bssid\s+([^\s]+)", output)

    if not ssid_match:
        return "󰖪 Offline"

    ssid = ssid_match.group(1).strip('"')

    status_match = re.search(r"\bstatus:\s+(\w+)", output)

    if status_match and status_match.group(1).lower() != "associated":
        return "󰖪 Offline"

    return f"󰖩 {ssid}"


# ==========================================================
# BLUETOOTH
# ==========================================================

def get_bluetooth_status() -> str:
    """
    Return a simple Bluetooth status.

    FreeBSD Bluetooth configurations vary significantly, so this
    checks whether the Bluetooth stack appears to be available.
    """

    ubt_devices = run_command(["sysctl", "-n", "net.bluetooth.hci.sockets.raw"])

    if ubt_devices:
        return "󰂯 On"

    dev_directory = Path("/dev")

    try:
        if any(dev_directory.glob("ubt*")):
            return "󰂯 On"
    except OSError:
        pass

    return "󰂲 Off"


# ==========================================================
# MEMORY
# ==========================================================

def get_memory_status():
    """
    Return memory usage in MB or GB.
    """

    try:
        import subprocess

        output = subprocess.check_output(
            ["sysctl", "-n", "hw.physmem"],
            text=True,
        ).strip()

        total = int(output)

        page_size = int(
            subprocess.check_output(
                ["sysctl", "-n", "hw.pagesize"],
                text=True,
            )
        )

        inactive = int(
            subprocess.check_output(
                ["sysctl", "-n", "vm.stats.vm.v_inactive_count"],
                text=True,
            )
        )

        cache = int(
            subprocess.check_output(
                ["sysctl", "-n", "vm.stats.vm.v_cache_count"],
                text=True,
            )
        )

        free = int(
            subprocess.check_output(
                ["sysctl", "-n", "vm.stats.vm.v_free_count"],
                text=True,
            )
        )

        available = (inactive + cache + free) * page_size
        used = total - available

        used_gb = used / (1024 ** 3)

        if used_gb >= 1:
            return f"󰍛 {used_gb:.1f}G"

        used_mb = used / (1024 ** 2)
        return f"󰍛 {used_mb:.0f}M"

    except Exception:
        return "󰍛 ?"


# ==========================================================
# CPU TEMPERATURE
# ==========================================================

def get_cpu_temperature() -> str:
    """
    Return the first available CPU temperature reading.
    """

    temperature_names = (
        "dev.cpu.0.temperature",
        "hw.acpi.thermal.tz0.temperature",
        "hw.acpi.thermal.tz1.temperature",
    )

    for name in temperature_names:
        value = read_sysctl(name)

        if not value:
            continue

        match = re.search(r"(-?\d+(?:\.\d+)?)", value)

        if match:
            temperature = float(match.group(1))
            return f" {temperature:.0f}°C"

    return " N/A"


# ==========================================================
# CPU USAGE
# ==========================================================

def get_cpu_usage() -> str:
    """
    Return the current CPU busy percentage using kern.cp_time.
    """

    first = read_sysctl("kern.cp_time")

    if not first:
        return " N/A"

    try:
        first_values = [int(value) for value in first.split()]

        if len(first_values) < 5:
            return " N/A"

        time.sleep(0.15)

        second = read_sysctl("kern.cp_time")
        second_values = [int(value) for value in second.split()]

        deltas = [
            second_value - first_value
            for first_value, second_value in zip(first_values, second_values)
        ]

        total_delta = sum(deltas)

        if total_delta <= 0:
            return " 0%"

        idle_delta = deltas[4]
        busy_percentage = 100 * (total_delta - idle_delta) / total_delta

        return f" {busy_percentage:.0f}%"

    except (ValueError, IndexError):
        return " N/A"


# ==========================================================
# NETWORK SPEED
# ==========================================================

def get_network_speed() -> str:
    """
    Return live download and upload speed for the selected interface.
    """

    global _net_previous_time
    global _net_previous_received
    global _net_previous_sent

    output = run_command(["netstat", "-b", "-I", NETWORK_INTERFACE])

    if not output:
        return "󰕒 N/A"

    lines = [
        line
        for line in output.splitlines()
        if NETWORK_INTERFACE in line
    ]

    if not lines:
        return "󰕒 N/A"

    fields = lines[-1].split()

    received: int | None = None
    sent: int | None = None

    numeric_values: list[int] = []

    for field in fields:
        if field.isdigit():
            numeric_values.append(int(field))

    if len(numeric_values) >= 2:
        received = numeric_values[-2]
        sent = numeric_values[-1]

    if received is None or sent is None:
        return "󰕒 N/A"

    current_time = time.monotonic()

    if (
        _net_previous_time is None
        or _net_previous_received is None
        or _net_previous_sent is None
    ):
        _net_previous_time = current_time
        _net_previous_received = received
        _net_previous_sent = sent

        return "󰇚 0B/s 󰕒 0B/s"

    elapsed = current_time - _net_previous_time

    if elapsed <= 0:
        return "󰇚 0B/s 󰕒 0B/s"

    received_difference = max(received - _net_previous_received, 0)
    sent_difference = max(sent - _net_previous_sent, 0)

    download_rate = received_difference / elapsed
    upload_rate = sent_difference / elapsed

    _net_previous_time = current_time
    _net_previous_received = received
    _net_previous_sent = sent

    return (
        f"󰇚 {format_rate(download_rate)} "
        f"󰕒 {format_rate(upload_rate)}"
    )


# ==========================================================
# VOLUME
# ==========================================================

def get_volume_status() -> str:
    """
    Return the FreeBSD mixer master volume.
    """

    output = run_command(["mixer", "vol"])

    if not output:
        return "󰕾 N/A"

    lowered = output.lower()

    if "mute" in lowered:
        return "󰝟 Muted"

    percentages = re.findall(r"(\d+(?:\.\d+)?)", output)

    if not percentages:
        return "󰕾 N/A"

    try:
        values = [float(value) for value in percentages]

        if all(value <= 1 for value in values):
            percentage = round(sum(values) / len(values) * 100)
        else:
            percentage = round(sum(values) / len(values))

    except ValueError:
        return "󰕾 N/A"

    if percentage <= 0:
        icon = "󰝟"
    elif percentage < 35:
        icon = "󰕿"
    elif percentage < 70:
        icon = "󰖀"
    else:
        icon = "󰕾"

    return f"{icon} {percentage}%"