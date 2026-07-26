"""Small, Fedora-native widget set for the Qtile bar."""

from libqtile import widget
from libqtile.lazy import lazy
from qtile_extras import widget as extra_widget

from colors import (
    accent,
    bar_background,
    bar_foreground,
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
    "padding": 5,
    "background": bar_background,
    "foreground": bar_foreground,
}
extension_defaults = widget_defaults.copy()


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
    return widget.TextBox(
        text="",
        foreground=accent,
        fontsize=18,
        padding=8,
        mouse_callbacks={"Button1": lazy.spawn(APPLICATION_LAUNCHER)},
    )


def groupbox():
    return widget.GroupBox(
        active=bar_foreground,
        inactive=workspace_inactive,
        urgent_alert_method="line",
        urgent_border=bar_foreground,
        highlight_method="line",
        highlight_color=[bar_background, bar_background],
        this_current_screen_border=bar_foreground,
        this_screen_border=bar_foreground,
        borderwidth=2,
        rounded=False,
        fontsize=WORKSPACE_ICON_SIZE,
        disable_drag=True,
        hide_unused=False,
        margin_y=3,
        padding_x=6,
    )


def window_name():
    return widget.WindowName(
        foreground=foreground_muted,
        fontsize=12,
        max_chars=55,
        empty_group_string="Desktop",
    )


def cpu():
    return widget.CPU(
        format=" {load_percent}%",
        foreground=bar_foreground,
        update_interval=CPU_UPDATE_INTERVAL,
        mouse_callbacks={"Button1": lazy.spawn(f"{TERMINAL} -e top")},
    )


def memory():
    return widget.Memory(
        format="󰍛 {MemUsed:.1f}{mm}",
        measure_mem="G",
        foreground=bar_foreground,
        update_interval=MEMORY_UPDATE_INTERVAL,
        mouse_callbacks={"Button1": lazy.spawn(f"{TERMINAL} -e top")},
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
    return widget.Mpris2(
        name="media",
        format="{xesam:title} — {xesam:artist}",
        playing_text=" {track}",
        paused_text=" {track}",
        stopped_text="",
        no_metadata_text="",
        scroll=True,
        width=360,
        foreground=bar_foreground,
    )


def battery():
    return widget.Battery(
        format="{char} {percent:2.0%}",
        charge_char="󰂄",
        discharge_char="󰁹",
        empty_char="󰂎",
        full_char="󰁹",
        foreground=bar_foreground,
        update_interval=BATTERY_UPDATE_INTERVAL,
    )


def clock():
    return widget.Clock(
        format="%a %b %d  %I:%M %p",
        width=230,
        padding=7,
        foreground=bar_foreground,
    )


def systray():
    return widget.Systray(icon_size=16, padding=5)


def power():
    return widget.TextBox(
        text="",
        foreground=bar_foreground,
        fontsize=17,
        padding=8,
        mouse_callbacks={"Button1": lazy.spawn(POWER_MENU)},
    )


def quick_settings():
    return widget.TextBox(
        text="󰒓",
        foreground=bar_foreground,
        fontsize=17,
        padding=8,
        mouse_callbacks={"Button1": lazy.spawn(script("quick-settings"))},
    )
