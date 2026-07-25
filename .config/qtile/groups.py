"""
Qtile workspaces (groups).

Every major application has a dedicated workspace.

When an application launches:
- it automatically opens in its assigned workspace
- Qtile automatically switches you to that workspace
"""

from libqtile.config import Group, Match
from libqtile.config import Key
from libqtile.lazy import lazy

from defaults import MOD


groups = [

    # Terminal
    Group(
        "1",
        label="",
        matches=[
            Match(wm_class="kitty"),
        ],
    ),

    # Browser
    Group(
        "2",
        label="󰈹",
        matches=[
            Match(wm_class="firefox"),
            Match(wm_class="LibreWolf"),
            Match(wm_class="chromium"),
            Match(wm_class="brave-browser"),
        ],
    ),

    # Development
    Group(
        "3",
        label="󰨞",
        matches=[
            Match(wm_class="Code"),
            Match(wm_class="code-oss"),
            Match(wm_class="VSCodium"),
            Match(wm_class="jetbrains-idea"),
        ],
    ),

    # Files
    Group(
        "4",
        label="",
        matches=[
            Match(wm_class="Thunar"),
            Match(wm_class="thunar"),
            Match(wm_class="Pcmanfm"),
            Match(wm_class="Nautilus"),
        ],
    ),

    # Media
    Group(
        "5",
        label="󰎄",
        matches=[
            Match(wm_class="vlc"),
            Match(wm_class="Spotify"),
            Match(wm_class="spotify"),
        ],
    ),

    # Communication
    Group(
        "6",
        label="󰭹",
        matches=[
            Match(wm_class="discord"),
            Match(wm_class="TelegramDesktop"),
            Match(wm_class="Signal"),
        ],
    ),

    # Misc
    Group(
        "7",
        label="󱂬",
    ),

    # Virtual Machines
    Group(
        "8",
        label="󰢹",
    ),

    # Scratch / Temporary
    Group(
        "9",
        label="",
    ),
]


def init_keys(keys):

    """
    Adds workspace shortcuts to the global keys list.
    """

    for group in groups:

        keys.extend(
            [

                # Switch workspace
                Key(
                    [MOD],
                    group.name,
                    lazy.group[group.name].toscreen(),
                ),

                # Move focused window and follow it
                Key(
                    [MOD, "shift"],
                    group.name,
                    lazy.window.togroup(
                        group.name,
                        switch_group=True,
                    ),
                ),

            ]
        )

    return keys