# Gruvbox Qtile desktop

A small, cohesive FreeBSD/X11 desktop tuned for the 2160×1350 display on a
ThinkPad X1 Nano Gen 1. One palette, one typeface, and one spacing system are
shared by Qtile, Rofi, Kitty, Dunst, GTK and Picom. The desktop deliberately
keeps effects and polling modest for good battery life.

## What is included

- **Qtile** — compact top bar, nine named workspaces and keyboard-first tiling.
- **Rofi** — application, window, power and quick-settings menus.
- **Kitty** — opaque-enough Gruvbox terminal with restrained padding.
- **Dunst** — matching, quiet notifications.
- **GTK 3** — Gruvbox theme preference and consistent font/icons.
- **Picom** — subtle shadows/fades without expensive blur.

## Install

Install `qtile`, `rofi`, `kitty`, `picom`, `dunst`, `feh`, `flameshot`,
`JetBrainsMono Nerd Font`, `Papirus-Dark`, and a GTK Gruvbox theme. Then link
this checkout into your home directory:

```sh
./install.sh
```

The installer only creates symlinks and moves an existing destination to a
timestamped backup. Set your wallpaper at `~/walls/wall1.jpg`, then start
Qtile from `.xinitrc` (or select it in your display manager).

## Essential keys

| Key | Action |
| --- | --- |
| `Super+d` | applications |
| `Super+Tab` | windows |
| `Super+Return` | terminal |
| `Super+a` | quick settings |
| `Super+Escape` | power menu |
| `Super+1…9` | change workspace |
| `Super+Shift+1…9` | move window and follow |
| `Super+h/j/k/l` | focus |
| `Super+Shift+h/j/k/l` | move window |

Hardware-specific values (display output, resolution and wallpaper) live in
`.config/qtile/defaults.py`. Run `qtile check -c ~/.config/qtile/config.py`
after changing the Qtile modules.
