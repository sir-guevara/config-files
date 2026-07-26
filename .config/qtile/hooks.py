"""
Qtile hooks.

Responsible for:

- Starting desktop services
- Wallpaper
- Display configuration
- Keyboard repeat rate
- Following applications to their dedicated workspaces
- Focusing newly opened windows
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

from libqtile import hook, qtile

from defaults import (
    DISPLAY_OUTPUT,
    DISPLAY_RESOLUTION,
    DUNST_CONFIG,
    KEY_REPEAT_DELAY,
    KEY_REPEAT_RATE,
    PICOM_CONFIG,
    WALLPAPER,
    script,
)


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def run(command):
    """Run a command silently."""

    try:
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except Exception:
        pass


# ---------------------------------------------------------
# Startup Once
# ---------------------------------------------------------

@hook.subscribe.startup_once
def startup_once():

    # Composite translucent windows with blur and rounded corners.
    run(["picom", "--daemon", "--config", str(PICOM_CONFIG)])

    # Lightweight desktop and hardware notifications.
    run(["dunst", "-conf", str(DUNST_CONFIG)])

    # NetworkManager lives in the existing Qtile system tray.
    run(["nm-applet"])

    # Restore the wallpaper without adding a desktop daemon.
    wallpaper = os.path.expanduser(str(WALLPAPER))
    if os.path.exists(wallpaper):
        run(["feh", "--no-fehbg", "--bg-fill", wallpaper])


# ---------------------------------------------------------
# Startup
# ---------------------------------------------------------

@hook.subscribe.startup
def startup():

    # Keep fonts and cursors readable on the native 2160x1350 X11 panel.
    run(["xrdb", "-merge", str(Path.home() / ".Xresources")])

    run([script("input-settings")])

    run([
        "xrandr",
        "--output",
        DISPLAY_OUTPUT,
        "--mode",
        DISPLAY_RESOLUTION,
    ])

    run([
        "xset",
        "r",
        "rate",
        str(KEY_REPEAT_DELAY),
        str(KEY_REPEAT_RATE),
    ])



# ---------------------------------------------------------
# Automatically follow applications
# ---------------------------------------------------------

@hook.subscribe.client_new
def follow_application(client):

    def switch():

        if client.group:

            if qtile.current_group != client.group:
                client.group.toscreen()

            client.focus(warp=False)

    qtile.call_later(0.10, switch)


# ---------------------------------------------------------
# Focus newly opened windows
# ---------------------------------------------------------

@hook.subscribe.client_managed
def focus_window(client):

    try:
        client.focus(warp=False)
    except Exception:
        pass
