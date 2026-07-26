"""Small, Fedora-native widget set for the Qtile bar."""

import os
import subprocess

from libqtile import widget
from libqtile.lazy import lazy
from qtile_extras import widget as extra_widget
from qtile_extras.widget.decorations import RectDecoration

from colors import (
    accent,
    bar_background,
    bar_foreground,
    surface,
    battery_color,
    bluetooth_color,
    cpu_color,
    foreground_muted,
    memory_color,
    power_color,
    volume_color,
    wifi_color,
    workspace_active,
    workspace_current,
    workspace_inactive,
    workspace_urgent,
)
from defaults import (
    APPLICATION_LAUNCHER,
    BATTERY_UPDATE_INTERVAL,
    CPU_UPDATE_INTERVAL,
    FONT,
    FONT_SIZE,
    MEMORY_UPDATE_INTERVAL,
    POWER_MENU,
    TERMINAL,
    WORKSPACE_ICON_SIZE,
    script,
)


widget_defaults = {
    "font": FONT,
    "fontsize": FONT_SIZE,
    "padding": 4,
    "background": bar_background,
    "foreground": bar_foreground,
}
extension_defaults = widget_defaults.copy()


def pill(colour=surface, radius=8):
    return [RectDecoration(filled=True, colour=colour, radius=radius)]


class StatusCommand(widget.GenPollCommand):
    """Use the bar color while active and muted gray while inactive."""

    def __init__(self, inactive_text, **config):
        self.inactive_text = inactive_text
        super().__init__(**config)

    async def apoll(self):
        text = await super().apoll()
        self.foreground = (
            foreground_muted if self.inactive_text in text else bar_foreground
        )
        return text


def separator():
    return widget.TextBox(text="·", foreground=foreground_muted, padding=4)


def launcher():
    return extra_widget.TextBox(
        text="",
        foreground=accent,
        fontsize=20,
        y_offset=1,
        padding=11,
        decorations=pill("#282828", 8),
        mouse_callbacks={"Button1": lazy.spawn(APPLICATION_LAUNCHER)},
    )


def groupbox():
    return extra_widget.GroupBox(
        active=bar_foreground,
        inactive=workspace_inactive,
        urgent_alert_method="line",
        urgent_border=bar_foreground,
        highlight_method="line",
        highlight_color=[bar_background, bar_background],
        this_current_screen_border=accent,
        this_screen_border=accent,
        borderwidth=3,
        rounded=True,
        fontsize=20,
        disable_drag=True,
        hide_unused=False,
        margin_y=4,
        padding_x=8,
        decorations=pill("#282828", 8),
    )


def window_name():
    return widget.WindowName(
        foreground="#83a598",
        fontsize=11,
        max_chars=42,
        empty_group_string="Ready",
        format="  {name}",
    )


def layout_name():
    return extra_widget.CurrentLayout(
        mode="text",
        foreground="#fabd2f",
        fontsize=10,
        padding=10,
        decorations=pill("#32302f", 8),
    )


def cpu():
    return extra_widget.CPU(
        format="󰍛 {load_percent:.0f}%",
        foreground="#fe8019",
        update_interval=CPU_UPDATE_INTERVAL,
        padding=9,
        decorations=pill("#282828", 8),
        mouse_callbacks={"Button1": lazy.spawn(f"{TERMINAL} -e top")},
    )


def memory():
    return extra_widget.Memory(
        format="󰘚 {MemUsed:.1f}G",
        measure_mem="G",
        foreground="#d3869b",
        update_interval=MEMORY_UPDATE_INTERVAL,
        padding=9,
        decorations=pill("#282828", 8),
        mouse_callbacks={"Button1": lazy.spawn(f"{TERMINAL} -e top")},
    )


def temperature():
    return extra_widget.GenPollCommand(
        cmd=[script("system-stat"), "temp"],
        update_interval=5,
        foreground="#fb4934",
        padding=9,
        decorations=pill("#282828", 8),
    )


def volume():
    return extra_widget.PulseVolumeExtra(
        name="volume",
        mode="bar",
        text_format="󰕾 {volume}%",
        bar_width=105,
        bar_colour_normal=bar_foreground,
        bar_colour_high=bar_foreground,
        bar_colour_loud=bar_foreground,
        bar_colour_mute=foreground_muted,
        hide_interval=86400,
        step=5,
        foreground=bar_foreground,
    )


def brightness():
    return extra_widget.BrightnessControl(
        name="brightness",
        mode="bar",
        text_format="󰃠 {percentage}%",
        bar_width=105,
        bar_colour=bar_foreground,
        timeout_interval=86400,
        step="5%",
        foreground=bar_foreground,
    )


def wifi():
    return StatusCommand(
        "Offline",
        cmd=[script("connectivity"), "wifi-status"],
        update_interval=5,
        foreground=foreground_muted,
        max_chars=20,
        mouse_callbacks={
            "Button1": lazy.spawn("nm-connection-editor"),
            "Button3": lazy.spawn(f'{script("connectivity")} wifi-toggle'),
        },
    )


def bluetooth():
    return StatusCommand(
        "Off",
        cmd=[script("connectivity"), "bluetooth-status"],
        update_interval=5,
        foreground=foreground_muted,
        mouse_callbacks={
            "Button1": lazy.spawn("blueman-manager"),
            "Button3": lazy.spawn(f'{script("connectivity")} bluetooth-toggle'),
        },
    )


def media():
    return widget.GenPollCommand(
        name="media",
        cmd=[script("bar-media"), "title"],
        update_interval=1,
        foreground="#83a598",
        padding=11,
        decorations=pill("#282828", 8),
        mouse_callbacks={
            "Button1": lazy.spawn("playerctl play-pause"),
            "Button4": lazy.spawn("playerctl next"),
            "Button5": lazy.spawn("playerctl previous"),
        },
    )


class MediaCover(widget.Image):
    """Small live MPRIS cover which disappears when no artwork exists."""

    def __init__(self, **config):
        super().__init__(
            filename=str(os.path.expanduser("~/.config/qtile/assets/transparent.svg")),
            margin=5,
            **config,
        )
        self._cover_path = ""

    def _configure(self, qtile, bar):
        super()._configure(qtile, bar)
        self.timeout_add(2, self._refresh)

    def _refresh(self):
        try:
            path = subprocess.check_output(
                [script("bar-media"), "cover"], text=True, timeout=10
            ).strip()
        except (OSError, subprocess.SubprocessError):
            path = ""
        if path and os.path.isfile(path) and path != self._cover_path:
            self._cover_path = path
            self.update(path)
        elif not path and self.img is not None:
            self._cover_path = ""
            self.img = None
            self.bar.draw()
        return 2


def media_cover():
    return MediaCover(background="#282828")


def battery():
    return extra_widget.Battery(
        format="{char} {percent:2.0%}",
        charge_char="󰂄",
        discharge_char="󰁹",
        empty_char="󰂎",
        full_char="󰁹",
        foreground="#b8bb26",
        update_interval=BATTERY_UPDATE_INTERVAL,
        padding=10,
        decorations=pill("#282828", 8),
    )


def clock():
    return widget.Clock(
        format="%a %d %b  %-I:%M %p",
        width=224,
        padding=7,
        foreground="#fbf1c7",
    )


def systray():
    return widget.Systray(icon_size=18, padding=7)


def power():
    return extra_widget.TextBox(
        text="󰐥",
        foreground="#fb4934",
        fontsize=20,
        y_offset=1,
        padding=10,
        decorations=pill("#282828", 8),
        mouse_callbacks={"Button1": lazy.spawn(POWER_MENU)},
    )


def quick_settings():
    return extra_widget.TextBox(
        text="󰒓",
        foreground="#8ec07c",
        fontsize=20,
        y_offset=1,
        padding=10,
        decorations=pill("#282828", 8),
        mouse_callbacks={"Button1": lazy.spawn(script("quick-settings"))},
    )
