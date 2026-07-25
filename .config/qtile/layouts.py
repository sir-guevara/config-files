"""
Qtile layouts.

All window layout styling lives here.
"""

from libqtile import layout

from colors import (
    border_focus,
    border_normal,
)

from defaults import (
    WINDOW_GAP,
    WINDOW_BORDER_WIDTH,
    FLOATING_BORDER_WIDTH,
    DEFAULT_LAYOUT_RATIO,
    LAYOUT_RATIO_STEP,
    MIN_LAYOUT_RATIO,
    MAX_LAYOUT_RATIO,
)


layouts = [

    layout.MonadTall(

        # Appearance
        border_focus=border_focus,
        border_normal=border_normal,

        border_width=WINDOW_BORDER_WIDTH,

        margin=WINDOW_GAP,

        single_border_width=WINDOW_BORDER_WIDTH,

        single_margin=WINDOW_GAP,

        # Behavior
        ratio=DEFAULT_LAYOUT_RATIO,
        min_ratio=MIN_LAYOUT_RATIO,
        max_ratio=MAX_LAYOUT_RATIO,
        ratio_increment=LAYOUT_RATIO_STEP,

        align=layout.MonadTall._left,

        change_ratio=0.05,
        change_size=20,

        new_client_position="after_current",

    ),

    layout.Max(),

    layout.Floating(

        border_focus=border_focus,
        border_normal=border_normal,
        border_width=FLOATING_BORDER_WIDTH,

    ),

]