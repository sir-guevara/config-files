"""
Qtile key bindings.
"""

from libqtile.config import Key
from libqtile.lazy import lazy

from defaults import (
    MOD,
    TERMINAL,
    BROWSER,
    CODE_EDITOR,
    EMAIL_CLIENT,
    FILE_MANAGER,
    MUSIC_PLAYER,
    APPLICATION_LAUNCHER,
    WINDOW_SWITCHER,
    POWER_MENU,
    script,
)


keys = [

    # -------------------------------------------------
    # Applications
    # -------------------------------------------------

    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Terminal"),

    Key(
        [MOD],
        "b",
        lazy.group["2"].toscreen(),
        lazy.spawn(BROWSER),
        desc="Browser",
    ),

    Key([MOD], "e", lazy.spawn(FILE_MANAGER), desc="File Manager"),

    Key(
        [MOD, "shift"],
        "f",
        lazy.group["2"].toscreen(),
        lazy.spawn(BROWSER),
        desc="Firefox",
    ),

    Key(
        [MOD, "shift"],
        "e",
        lazy.group["5"].toscreen(),
        lazy.spawn(EMAIL_CLIENT),
        desc="Thunderbird",
    ),

    Key([MOD, "shift"], "m", lazy.spawn(MUSIC_PLAYER), desc="Music"),

    Key([MOD, "shift"], "c", lazy.spawn(CODE_EDITOR), desc="VS Code"),

    Key([MOD, "shift"], "t", lazy.spawn(FILE_MANAGER), desc="Thunar"),

    Key([MOD], "d", lazy.spawn(APPLICATION_LAUNCHER), desc="Application Launcher"),

    Key([MOD], "space", lazy.spawn(APPLICATION_LAUNCHER), desc="Application Launcher"),

    Key([MOD], "Tab", lazy.spawn(WINDOW_SWITCHER), desc="Window Switcher"),

    Key([MOD], "a", lazy.spawn(script("quick-settings")), desc="Quick Settings"),

    Key([], "Print", lazy.spawn("flameshot gui"), desc="Screenshot"),

    Key([MOD, "shift"], "s", lazy.spawn("flameshot gui"), desc="Screenshot"),

    Key(
        [MOD, "shift"],
        "w",
        lazy.spawn(script("wallpaper-next")),
        desc="Next Wallpaper",
    ),
    # -------------------------------------------------
    # Qtile
    # -------------------------------------------------

    Key([MOD], "q", lazy.window.kill()),

    Key([MOD, "control"], "r", lazy.reload_config()),

    Key([MOD, "control"], "q", lazy.shutdown()),

    # -------------------------------------------------
    # Focus
    # -------------------------------------------------

    Key([MOD], "h", lazy.layout.left()),

    Key([MOD], "j", lazy.layout.down()),

    Key([MOD], "k", lazy.layout.up()),

    Key([MOD], "l", lazy.layout.right()),

    # -------------------------------------------------
    # Move Windows
    # -------------------------------------------------

    Key([MOD, "shift"], "h", lazy.layout.shuffle_left()),

    Key([MOD, "shift"], "j", lazy.layout.shuffle_down()),

    Key([MOD, "shift"], "k", lazy.layout.shuffle_up()),

    Key([MOD, "shift"], "l", lazy.layout.shuffle_right()),

    # -------------------------------------------------
    # Resize
    # -------------------------------------------------

    Key([MOD, "control"], "h", lazy.layout.grow()),

    Key([MOD, "control"], "j", lazy.layout.grow_down()),

    Key([MOD, "control"], "k", lazy.layout.grow_up()),

    Key([MOD, "control"], "l", lazy.layout.shrink()),

    Key([MOD], "n", lazy.layout.normalize()),

    # -------------------------------------------------
    # Layout
    # -------------------------------------------------

    Key([MOD], "f", lazy.window.toggle_fullscreen()),

    Key([MOD, "shift"], "space", lazy.next_layout()),

    # -------------------------------------------------
    # Power Menu
    # -------------------------------------------------

    Key(
        [MOD],
        "Escape",
        lazy.spawn(POWER_MENU),
    ),

    # -------------------------------------------------
    # Audio
    # -------------------------------------------------

    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn(script("volume") + " up"),
    ),

    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn(script("volume") + " down"),
    ),

    Key(
        [],
        "XF86AudioMute",
        lazy.spawn(script("volume") + " mute"),
    ),

    # -------------------------------------------------
    # Brightness
    # -------------------------------------------------

    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn(script("brightness") + " up"),
    ),

    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn(script("brightness") + " down"),
    ),
]
