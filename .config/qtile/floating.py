"""
Floating window rules.

Any application listed here will automatically float instead of
being tiled.
"""

from libqtile.config import Match
from libqtile.layout import Floating

from colors import (
    border_focus,
    border_normal,
)

from defaults import (
    FLOATING_BORDER_WIDTH,
)


floating_layout = Floating(

    border_focus=border_focus,
    border_normal=border_normal,
    border_width=FLOATING_BORDER_WIDTH,

    float_rules=[

        # Default Qtile rules
        *Floating.default_float_rules,

        # Authentication dialogs
        Match(title="Authentication"),
        Match(title="Authentication Required"),
        Match(title="Open File"),
        Match(title="Save File"),
        Match(title="File Operation Progress"),

        # Confirmations
        Match(title="Confirm"),
        Match(title="Confirmation"),
        Match(title="Warning"),
        Match(title="Error"),

        # File picker dialogs
        Match(wm_class="zenity"),
        Match(wm_class="Yad"),
        Match(wm_class="Pavucontrol"),
        Match(wm_class="Lxinput"),
        Match(wm_class="Arandr"),

        # Rofi
        Match(wm_class="rofi"),

        # Image viewers
        Match(wm_class="feh"),

        # mpv
        Match(wm_class="mpv"),

        # SSH askpass
        Match(title="SSH Askpass"),

    ],
)
