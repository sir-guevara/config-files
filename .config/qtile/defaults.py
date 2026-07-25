"""
Shared Qtile defaults and application commands.

This file keeps common paths, commands, fonts, dimensions,
and desktop settings in one place.
"""

from pathlib import Path


# ==========================================================
# PATHS
# ==========================================================

HOME = Path.home()

CONFIG_DIR = HOME / ".config"
QTILE_DIR = CONFIG_DIR / "qtile"
SCRIPTS_DIR = QTILE_DIR / "scripts"
THEMES_DIR = QTILE_DIR / "themes"

WALLPAPER_DIR = HOME / "walls"
WALLPAPER = WALLPAPER_DIR / "wall1.jpg"


# ==========================================================
# MODIFIER KEY
# ==========================================================

MOD = "mod4"


# ==========================================================
# APPLICATIONS
# ==========================================================

TERMINAL = "kitty"
BROWSER = "firefox"
FILE_MANAGER = "thunar"
EDITOR = "code-oss"

APPLICATION_LAUNCHER = "rofi -show drun"
WINDOW_SWITCHER = "rofi -show window"

POWER_MENU = str(SCRIPTS_DIR / "power-menu")
WIFI_MENU = str(SCRIPTS_DIR / "wifi-menu")
BLUETOOTH_MENU = str(SCRIPTS_DIR / "bluetooth-menu")


# ==========================================================
# FONTS
# ==========================================================

FONT = "JetBrainsMono Nerd Font"
FONT_BOLD = "JetBrainsMono Nerd Font Bold"

FONT_SIZE = 14
BAR_ICON_SIZE = 17
WORKSPACE_ICON_SIZE = 20


# ==========================================================
# WINDOW STYLING
# ==========================================================

WINDOW_GAP = 8
WINDOW_BORDER_WIDTH = 2

FLOATING_BORDER_WIDTH = 2

MIN_LAYOUT_RATIO = 0.25
DEFAULT_LAYOUT_RATIO = 0.55
MAX_LAYOUT_RATIO = 0.75
LAYOUT_RATIO_STEP = 0.05


# ==========================================================
# BAR STYLING
# ==========================================================

BAR_HEIGHT = 34

BAR_MARGIN_TOP = 8
BAR_MARGIN_RIGHT = 12
BAR_MARGIN_BOTTOM = 0
BAR_MARGIN_LEFT = 12

BAR_MARGIN = [
    BAR_MARGIN_TOP,
    BAR_MARGIN_RIGHT,
    BAR_MARGIN_BOTTOM,
    BAR_MARGIN_LEFT,
]

BAR_OPACITY = 0.98

BAR_PADDING = 6
BAR_SECTION_SPACING = 8


# ==========================================================
# WIDGET UPDATE INTERVALS
# ==========================================================

BATTERY_UPDATE_INTERVAL = 10
WIFI_UPDATE_INTERVAL = 5
BLUETOOTH_UPDATE_INTERVAL = 10
MEMORY_UPDATE_INTERVAL = 3
CPU_UPDATE_INTERVAL = 3
TEMPERATURE_UPDATE_INTERVAL = 5
NETWORK_UPDATE_INTERVAL = 2
VOLUME_UPDATE_INTERVAL = 1


# ==========================================================
# DISPLAY
# ==========================================================

DISPLAY_OUTPUT = "eDP-1"
DISPLAY_RESOLUTION = "2160x1350"


# ==========================================================
# KEYBOARD
# ==========================================================

KEY_REPEAT_DELAY = 300
KEY_REPEAT_RATE = 50


# ==========================================================
# COMMAND HELPERS
# ==========================================================

def script(name: str) -> str:
    """
    Return the full path to a script inside the Qtile scripts directory.
    """

    return str(SCRIPTS_DIR / name)
    