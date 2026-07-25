"""
Minimalist Qtile widget definitions.

FreeBSD-specific information is provided by system.py.
"""

from libqtile import widget
from libqtile.lazy import lazy

from colors import (
    accent,
    bar_background,
    bar_foreground,
    battery_color,
    bluetooth_color,
    clock_color,
    cpu_color,
    foreground_muted,
    memory_color,
    network_color,
    power_color,
    temperature_color,
    volume_color,
    wifi_color,
    workspace_active,
    workspace_current,
    workspace_inactive,
    workspace_urgent,
)

from defaults import (
    BAR_ICON_SIZE,
    BATTERY_UPDATE_INTERVAL,
    BLUETOOTH_UPDATE_INTERVAL,
    CPU_UPDATE_INTERVAL,
    FONT,
    FONT_SIZE,
    MEMORY_UPDATE_INTERVAL,
    NETWORK_UPDATE_INTERVAL,
    POWER_MENU,
    TEMPERATURE_UPDATE_INTERVAL,
    VOLUME_UPDATE_INTERVAL,
    WIFI_UPDATE_INTERVAL,
    WORKSPACE_ICON_SIZE,
)

from system import (
    get_battery_status,
    get_bluetooth_status,
    get_cpu_temperature,
    get_cpu_usage,
    get_memory_status,
    get_network_speed,
    get_volume_status,
    get_wifi_status,
)


# ==========================================================
# COMMANDS
# ==========================================================

LAUNCHER = (
    "rofi -show drun "
    "-show-icons "
    "-theme ~/.config/rofi/gruvbox.rasi"
)

QUICK_SETTINGS = "~/.config/qtile/scripts/quick-settings"


# ==========================================================
# GLOBAL DEFAULTS
# ==========================================================

widget_defaults = {
    "font": FONT,
    "fontsize": FONT_SIZE,
    "padding": 4,
    "background": bar_background,
    "foreground": bar_foreground,
}

extension_defaults = widget_defaults.copy()


# ==========================================================
# HELPERS
# ==========================================================

def spacer(length: int = 6):
    """Small fixed space."""

    return widget.Spacer(length=length)


def flexible_spacer():
    """Flexible space used to center widgets."""

    return widget.Spacer()


def separator():
    """Minimal section separator."""

    return widget.TextBox(
        text="|",
        foreground=foreground_muted,
        fontsize=11,
        padding=5,
    )


def icon(
    text: str,
    color: str = accent,
    size: int = BAR_ICON_SIZE,
):
    """Minimal icon widget."""

    return widget.TextBox(
        text=text,
        foreground=color,
        fontsize=size,
        padding=4,
    )



# ==========================================================
# LEFT SIDE
# ==========================================================

def launcher():
    """Open the application launcher."""

    return widget.TextBox(
        text="",
        foreground=accent,
        fontsize=17,
        padding=7,
        mouse_callbacks={
            "Button1": lazy.spawn(LAUNCHER),
        },
    )


def groupbox():
    """Minimal workspace switcher."""
    size: int = WORKSPACE_ICON_SIZE
    return widget.GroupBox(
        active=workspace_active,
        inactive=workspace_inactive,
        urgent_alert_method="line",
        urgent_border=workspace_urgent,
        highlight_method="line",
        highlight_color=[
            bar_background,
            bar_background,
        ],
        this_current_screen_border=workspace_current,
        this_screen_border=workspace_current,
        other_current_screen_border=foreground_muted,
        other_screen_border=foreground_muted,
        borderwidth=2,
        rounded=False,
        fontsize=size,
        disable_drag=True,
        use_mouse_wheel=True,
        hide_unused=False,
        margin_y=3,
        margin_x=4,
        padding_y=3,
        padding_x=6,
    )


def current_layout():
    """Display the current layout icon."""

    return widget.CurrentLayout(
        mode="icon",
        scale=0.50,
        padding=4,
    )


def window_name():
    """Display the focused window title."""

    return widget.WindowName(
        foreground=foreground_muted,
        fontsize=12,
        padding=6,
        max_chars=42,
        empty_group_string="Desktop",
    )


# ==========================================================
# CENTER
# ==========================================================

def clock():
    """Centered date and time."""

    return widget.Clock(
        format="%a %b %d  %I:%M %p",
        foreground=clock_color,
        fontsize=11,
        padding=7,
    )


# ==========================================================
# RIGHT SIDE
# ==========================================================

def memory():
    """Display memory usage."""

    return widget.GenPollText(
        func=get_memory_status,
        update_interval=MEMORY_UPDATE_INTERVAL,
        foreground=memory_color,
        padding=4,
        mouse_callbacks={
            "Button1": lazy.spawn("kitty -e top"),
        },
    )


def cpu():
    """Display CPU usage."""

    return widget.GenPollText(
        func=get_cpu_usage,
        update_interval=CPU_UPDATE_INTERVAL,
        foreground=cpu_color,
        padding=4,
        mouse_callbacks={
            "Button1": lazy.spawn("kitty -e top"),
        },
    )


def temperature():
    """Display CPU temperature."""

    return widget.GenPollText(
        func=get_cpu_temperature,
        update_interval=TEMPERATURE_UPDATE_INTERVAL,
        foreground=temperature_color,
        padding=4,
    )


def network_speed():
    """Display network upload and download speed."""

    return widget.GenPollText(
        func=get_network_speed,
        update_interval=NETWORK_UPDATE_INTERVAL,
        foreground=network_color,
        padding=4,
    )


def wifi():
    """Display Wi-Fi status and open Quick Settings."""

    return widget.GenPollText(
        func=get_wifi_status,
        update_interval=WIFI_UPDATE_INTERVAL,
        foreground=wifi_color,
        padding=4,
        mouse_callbacks={
            "Button1": lazy.spawn(QUICK_SETTINGS),
        },
    )


def bluetooth():
    """Display Bluetooth status and open Quick Settings."""

    return widget.GenPollText(
        func=get_bluetooth_status,
        update_interval=BLUETOOTH_UPDATE_INTERVAL,
        foreground=bluetooth_color,
        padding=4,
        mouse_callbacks={
            "Button1": lazy.spawn(QUICK_SETTINGS),
        },
    )


def volume():
    """Display volume and provide mouse controls."""

    return widget.GenPollText(
        func=get_volume_status,
        update_interval=VOLUME_UPDATE_INTERVAL,
        foreground=volume_color,
        padding=4,
        mouse_callbacks={
            "Button1": lazy.spawn(QUICK_SETTINGS),
            "Button2": lazy.spawn("mixer vol.mute=toggle"),
            "Button4": lazy.spawn("mixer vol=+5%"),
            "Button5": lazy.spawn("mixer vol=-5%"),
        },
    )


def battery():
    """Display battery status and open Quick Settings."""

    return widget.GenPollText(
        func=get_battery_status,
        update_interval=BATTERY_UPDATE_INTERVAL,
        foreground=battery_color,
        padding=4,
        mouse_callbacks={
            "Button1": lazy.spawn(QUICK_SETTINGS),
        },
    )


def systray():
    """Display background application icons."""

    return widget.Systray(
        icon_size=15,
        padding=4,
    )


def notification_indicator():
    """Open or clear Dunst notifications."""

    return widget.TextBox(
        text="󰂚",
        foreground=bar_foreground,
        fontsize=BAR_ICON_SIZE,
        padding=5,
        mouse_callbacks={
            "Button1": lazy.spawn("dunstctl history-pop"),
            "Button3": lazy.spawn("dunstctl close-all"),
        },
    )


def quick_settings():
    """Dedicated Quick Settings button."""

    return widget.TextBox(
        text="󰒓",
        foreground=accent,
        fontsize=BAR_ICON_SIZE,
        padding=6,
        mouse_callbacks={
            "Button1": lazy.spawn(QUICK_SETTINGS),
        },
    )


def power():
    """Open the power dashboard."""

    return widget.TextBox(
        text="",
        foreground=power_color,
        fontsize=BAR_ICON_SIZE,
        padding=7,
        mouse_callbacks={
            "Button1": lazy.spawn(POWER_MENU),
        },
    )