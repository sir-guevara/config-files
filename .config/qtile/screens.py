"""
Qtile screen and top-bar configuration.

The bar is arranged in three visual sections:

Left:
- launcher
- workspaces
- current layout
- focused window title

Center:
- date and time

Right:
- memory
- CPU
- temperature
- network speed
- Wi-Fi
- Bluetooth
- volume
- battery
- system tray
- notifications
- power menu
"""

from libqtile import bar
from libqtile.config import Screen

from colors import bar_background

from defaults import (
    BAR_HEIGHT,
    BAR_MARGIN,
)

from widgets import (
    battery,
    bluetooth,
    clock,
    cpu,
    current_layout,
    flexible_spacer,
    groupbox,
    launcher,
    memory,
    network_speed,
    notification_indicator,
    power,
    separator,
    spacer,
    systray,
    temperature,
    volume,
    wifi,
    quick_settings,
    window_name,
)


def primary_bar():
    """
    Build the primary Qtile top bar.
    """

    return bar.Bar(
        widgets=[
            # ==================================================
            # LEFT SECTION
            # ==================================================

            launcher(),

            spacer(4),

            groupbox(),

            spacer(4),

            current_layout(),

            spacer(4),

            window_name(),

            # Expands to push the clock toward the center.
            flexible_spacer(),

            # ==================================================
            # CENTER SECTION
            # ==================================================

            clock(),

            # Matches the left flexible spacer and keeps the
            # clock centered across the full screen.
            flexible_spacer(),

            # ==================================================
            # RIGHT SECTION
            # ==================================================

            memory(),

            separator(),

            cpu(),

            separator(),

            temperature(),

            separator(),

            wifi(),

            separator(),

            bluetooth(),

            separator(),

            volume(),

            separator(),

            battery(),

            separator(),

            systray(),
            notification_indicator(),
            quick_settings(),

            power(),
        ],

        size=BAR_HEIGHT,

        background=bar_background,

        margin=BAR_MARGIN,

        opacity=1.0,
    )


screens = [
    Screen(
        top=primary_bar(),
    ),
]