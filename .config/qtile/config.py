"""
Main Qtile configuration.

This file assembles the separate Qtile modules.
"""

# Importing hooks registers all subscribed Qtile hooks.
import hooks  # noqa: F401

from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from defaults import MOD
from floating import floating_layout
from groups import groups, init_keys
from keys import keys
from layouts import layouts
from screens import screens
from widgets import extension_defaults, widget_defaults


# ==========================================================
# WORKSPACE KEY BINDINGS
# ==========================================================

# Add workspace navigation shortcuts to the main key list.
#
# Super + number:
# Switch to the workspace.
#
# Super + Shift + number:
# Move the focused window to the workspace and follow it.
keys = init_keys(keys)


# ==========================================================
# MOUSE BINDINGS
# ==========================================================

mouse = [
    # Super + left-click:
    # Move a floating window.
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),

    # Super + right-click:
    # Resize a floating window.
    Drag(
        [MOD],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),

    # Super + middle-click:
    # Bring the selected window to the front.
    Click(
        [MOD],
        "Button2",
        lazy.window.bring_to_front(),
    ),
]


# ==========================================================
# DYNAMIC GROUP SETTINGS
# ==========================================================

# We define workspace shortcuts manually in groups.py.
dgroups_key_binder = None

# Applications are assigned through Match rules in groups.py.
#
# The explicit annotation prevents Qtile's mypy checker from
# reporting that the empty list has an unknown item type.
dgroups_app_rules: list[object] = []


# ==========================================================
# WINDOW FOCUS
# ==========================================================

# Focus a window when the mouse pointer enters it.
follow_mouse_focus = True

# Do not automatically raise every window when it is clicked.
bring_front_click = False

# Do not move the pointer when keyboard focus changes.
cursor_warp = False

# Newly opened windows can request focus when appropriate.
focus_on_window_activation = "smart"


# ==========================================================
# FLOATING AND FULLSCREEN BEHAVIOR
# ==========================================================

# Keep floating windows above tiled windows.
floats_kept_above = True

# Honor fullscreen requests from applications.
auto_fullscreen = True

# Do not automatically minimize applications.
auto_minimize = False


# ==========================================================
# DISPLAY BEHAVIOR
# ==========================================================

# Reconfigure Qtile when monitor configuration changes.
reconfigure_screens = True


# ==========================================================
# JAVA APPLICATION COMPATIBILITY
# ==========================================================

wmname = "Qtile"