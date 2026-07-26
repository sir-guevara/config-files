"""Single-screen layout for the X1 Nano display."""

from libqtile import bar, widget
from libqtile.config import Screen

from colors import bar_background
from defaults import BAR_HEIGHT, BAR_MARGIN
from widgets import (
    battery,
    clock,
    groupbox,
    launcher,
    power,
    quick_settings,
    systray,
)


def primary_bar():
    return bar.Bar(
        [
            launcher(),
            groupbox(),
            widget.Spacer(),
            clock(),
            widget.Spacer(),
            battery(),
            systray(),
            quick_settings(),
            power(),
        ],
        size=BAR_HEIGHT,
        background=bar_background,
        margin=BAR_MARGIN,
        opacity=1.0,
    )


screens = [Screen(top=primary_bar())]
