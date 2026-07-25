"""
Shared Gruvbox color palette for the Qtile desktop.

Every Qtile module will import colors from this file so the
desktop remains visually consistent and easy to customize.
"""

colors = {
    # Backgrounds
    "bg0_hard": "#1d2021",
    "bg0": "#282828",
    "bg0_soft": "#32302f",
    "bg1": "#3c3836",
    "bg2": "#504945",
    "bg3": "#665c54",
    "bg4": "#7c6f64",

    # Foregrounds
    "fg0": "#fbf1c7",
    "fg1": "#ebdbb2",
    "fg2": "#d5c4a1",
    "fg3": "#bdae93",
    "fg4": "#a89984",

    # Neutral
    "gray": "#928374",

    # Bright Gruvbox colors
    "red": "#fb4934",
    "green": "#b8bb26",
    "yellow": "#fabd2f",
    "blue": "#83a598",
    "purple": "#d3869b",
    "aqua": "#8ec07c",
    "orange": "#fe8019",

    # Dark Gruvbox colors
    "dark_red": "#cc241d",
    "dark_green": "#98971a",
    "dark_yellow": "#d79921",
    "dark_blue": "#458588",
    "dark_purple": "#b16286",
    "dark_aqua": "#689d6a",
    "dark_orange": "#d65d0e",
}


# Main desktop colors
background = colors["bg0_hard"]
background_alt = colors["bg0"]
surface = colors["bg1"]
surface_alt = colors["bg2"]

foreground = colors["fg1"]
foreground_bright = colors["fg0"]
foreground_muted = colors["gray"]

accent = colors["orange"]
accent_secondary = colors["yellow"]

success = colors["green"]
warning = colors["yellow"]
error = colors["red"]
info = colors["blue"]


# Qtile-specific colors
border_focus = colors["orange"]
border_normal = colors["bg1"]
border_floating = colors["yellow"]

bar_background = colors["bg0_hard"]
bar_foreground = colors["fg1"]

workspace_active = colors["fg0"]
workspace_inactive = colors["gray"]
workspace_current = colors["orange"]
workspace_urgent = colors["red"]

clock_color = colors["fg0"]
battery_color = colors["green"]
wifi_color = colors["aqua"]
bluetooth_color = colors["blue"]
memory_color = colors["purple"]
cpu_color = colors["orange"]
temperature_color = colors["red"]
network_color = colors["blue"]
volume_color = colors["yellow"]
power_color = colors["red"]