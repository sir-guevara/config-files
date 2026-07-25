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
import shutil
import subprocess

from libqtile import hook, qtile

from defaults import (
    DISPLAY_OUTPUT,
    DISPLAY_RESOLUTION,
    KEY_REPEAT_DELAY,
    KEY_REPEAT_RATE,
    WALLPAPER,
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


def run_once(command, process=None):
    """
    Run a command only if it is not already running.
    """

    process = process or os.path.basename(command[0])

    try:
        if subprocess.call(
            ["pgrep", "-x", process],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ):
            run(command)
    except Exception:
        pass


# ---------------------------------------------------------
# Startup Once
# ---------------------------------------------------------

@hook.subscribe.startup_once
def startup_once():

    # Compositor
    run_once(["picom"])

    # Notification daemon
    run_once(["dunst"])

    # Clipboard manager
    run_once(["copyq"])

    # LXQt PolicyKit Agent
    lxqt_agent = shutil.which("lxqt-policykit-agent")

    if lxqt_agent:
        run_once(
            [lxqt_agent],
            process="lxqt-policykit-agent",
        )


# ---------------------------------------------------------
# Startup
# ---------------------------------------------------------

@hook.subscribe.startup
def startup():

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

    wallpaper = os.path.expanduser(str(WALLPAPER))

    if os.path.exists(wallpaper):

        run([
            "feh",
            "--bg-fill",
            wallpaper,
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