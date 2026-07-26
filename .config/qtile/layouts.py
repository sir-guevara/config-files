"""Purpose-built layouts for the Gruvbox Ember desktop."""

from libqtile import layout

from colors import border_normal
from defaults import (
    DEFAULT_LAYOUT_RATIO,
    LAYOUT_RATIO_STEP,
    MAX_LAYOUT_RATIO,
    MIN_LAYOUT_RATIO,
    WINDOW_BORDER_WIDTH,
    WINDOW_GAP,
)


common = {
    "border_normal": border_normal,
    "border_width": WINDOW_BORDER_WIDTH,
    "margin": WINDOW_GAP,
}


layouts = [
    # Forge: editor or terminal in the master pane, references on the right.
    layout.MonadTall(
        name="Forge",
        border_focus="#fe8019",
        single_border_width=WINDOW_BORDER_WIDTH,
        single_margin=WINDOW_GAP,
        ratio=DEFAULT_LAYOUT_RATIO,
        min_ratio=MIN_LAYOUT_RATIO,
        max_ratio=MAX_LAYOUT_RATIO,
        ratio_increment=LAYOUT_RATIO_STEP,
        align=layout.MonadTall._left,
        change_ratio=0.05,
        change_size=20,
        new_client_position="after_current",
        **common,
    ),
    # Lounge: horizontal hierarchy for browsers, mail and wide displays.
    layout.MonadWide(
        name="Lounge",
        border_focus="#d3869b",
        single_border_width=WINDOW_BORDER_WIDTH,
        single_margin=WINDOW_GAP,
        ratio=0.68,
        min_ratio=MIN_LAYOUT_RATIO,
        max_ratio=0.82,
        ratio_increment=LAYOUT_RATIO_STEP,
        change_ratio=0.04,
        change_size=20,
        new_client_position="after_current",
        **common,
    ),
    # Gallery: fluid columns are ideal for file managers and comparisons.
    layout.Columns(
        name="Gallery",
        border_focus="#83a598",
        border_focus_stack="#8ec07c",
        num_columns=3,
        grow_amount=28,
        fair=True,
        wrap_focus_columns=True,
        wrap_focus_rows=True,
        **common,
    ),
    # Mosaic: organic BSP splits for terminals and exploratory work.
    layout.Bsp(
        name="Mosaic",
        border_focus="#8ec07c",
        ratio=1.55,
        grow_amount=24,
        fair=False,
        **common,
    ),
    # Stage: one window owns the scene; others remain behind it.
    layout.Max(
        name="Stage",
        border_focus="#fabd2f",
        margin=WINDOW_GAP,
        border_normal=border_normal,
        border_width=WINDOW_BORDER_WIDTH,
    ),
]
