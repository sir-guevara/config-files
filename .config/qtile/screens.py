"""Single-screen layout for the X1 Nano display."""

from libqtile import bar, widget
from libqtile.config import Screen

from colors import bar_background
from defaults import BAR_HEIGHT, BAR_MARGIN
from widgets import (
    battery,
    clock,
    cpu,
    groupbox,
    launcher,
    media,
    media_cover,
    memory,
    power,
    quick_settings,
    systray,
    temperature,
)


def primary_bar():
    return bar.Bar(
        [
            launcher(),
            widget.Spacer(length=6),
            groupbox(),
            widget.Spacer(),
            media_cover(),
            widget.Spacer(length=4),
            media(),
            widget.TextBox(text="•", foreground="#a89984", fontsize=12, padding=7),
            clock(),
            widget.Spacer(),
            cpu(),
            widget.Spacer(length=4),
            memory(),
            widget.Spacer(length=4),
            temperature(),
            widget.Spacer(length=5),
            battery(),
            widget.Spacer(length=5),
            systray(),
            widget.Spacer(length=5),
            quick_settings(),
            widget.Spacer(length=5),
            power(),
            widget.Spacer(length=8),
        ],
        size=BAR_HEIGHT,
        background="#00000000",
        margin=BAR_MARGIN,
        opacity=1.0,
    )


screens = [Screen(top=primary_bar())]
