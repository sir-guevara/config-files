"""Dedicated workspaces and application routing rules."""

import re

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from defaults import MOD


def match_classes(*names: str) -> Match:
    """Match any listed X11/Wayland application class exactly."""

    pattern = "|".join(re.escape(name) for name in names)
    return Match(wm_class=re.compile(rf"^(?:{pattern})$", re.IGNORECASE))


groups = [
    Group(
        "1",
        label="",
        layout="Forge",
        matches=[match_classes("Alacritty", "kitty", "org.wezfurlong.wezterm")],
    ),
    Group(
        "2",
        label="󰈹",
        layout="Forge",
        matches=[
            match_classes(
                "firefox",
                "firefox-esr",
                "org.mozilla.firefox",
                "Navigator",
                "Google-chrome",
                "Chromium",
                "Brave-browser",
            )
        ],
    ),
    Group(
        "3",
        label="󰨞",
        layout="Forge",
        matches=[
            match_classes(
                "Code",
                "code-oss",
                "VSCodium",
                "Sublime_text",
                "jetbrains-idea",
            )
        ],
    ),
    Group(
        "4",
        label="",
        layout="Forge",
        matches=[match_classes("Thunar", "Nautilus", "org.gnome.Nautilus", "dolphin")],
    ),
    Group(
        "5",
        label="",
        layout="Forge",
        matches=[
            match_classes(
                "thunderbird",
                "org.mozilla.Thunderbird",
                "evolution",
                "Mailspring",
            )
        ],
    ),
    Group(
        "6",
        label="󰎄",
        layout="Forge",
        matches=[match_classes("Cider", "cider", "Spotify", "Rhythmbox", "strawberry")],
    ),
    Group("7", label="", layout="Forge"),
]


def init_keys(keys):
    for group in groups:
        keys.extend(
            [
                Key([MOD], group.name, lazy.group[group.name].toscreen()),
                Key(
                    [MOD, "shift"],
                    group.name,
                    lazy.window.togroup(group.name, switch_group=True),
                ),
            ]
        )
    return keys
