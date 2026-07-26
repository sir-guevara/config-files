# Minimal Gruvbox Qtile desktop

A small Fedora/X11 setup for a ThinkPad X1 Nano Gen 1 (2160×1350). The tracked
desktop is deliberately limited to Qtile, Alacritty, feh, Rofi, Thunar,
Starship, and the GTK settings needed to keep Thunar visually consistent.

## Included

- **Qtile** — five workspaces and a compact, battery-conscious bar
- **Alacritty** — Gruvbox terminal
- **Rofi** — Gruvbox application, window, and power menus
- **feh** — static wallpaper, with no desktop daemon
- **Thunar** — lightweight file manager
- **Starship** — short Gruvbox shell prompt
- **GTK 3** — Gruvbox theme, Papirus icons, and matching fonts

The old FreeBSD commands, Kitty, Eww, Picom, Dunst, duplicate quick settings,
and their helper scripts have been removed.

## Fedora packages

Install the core applications and small runtime helpers:

```sh
sudo dnf install qtile alacritty rofi thunar feh brightnessctl \
  wireplumber starship dbus-x11 xorg-x11-xinit xorg-x11-server-utils \
  papirus-icon-theme NetworkManager-wifi nm-connection-editor \
  bluez blueman network-manager-applet pavucontrol playerctl \
  lxinput arandr python3-pip

python3 -m pip install --user qtile-extras
```

Install a Gruvbox GTK theme separately and make sure its installed name matches
`Gruvbox-Dark-BL` in `.config/gtk-3.0/settings.ini` and `.xinitrc`. Install the
JetBrainsMono Nerd Font as well; the regular Fedora JetBrains Mono package does
not include the icon glyphs used by the bar and prompt.

## Link the dotfiles

```sh
./install.sh
```

The installer links individual files, backs up regular files before replacing
them, and removes obsolete symlinks from earlier versions of this repository.
Put the wallpaper at `~/walls/wall1.jpg`.

Enable Starship in the shell you actually use:

```sh
# Bash: add to ~/.bashrc
eval "$(starship init bash)"

# Zsh: add to ~/.zshrc instead
eval "$(starship init zsh)"
```

Start X with `startx`, or select Qtile from a display manager.

## Keys

| Key | Action |
| --- | --- |
| `Super+d` | applications |
| `Super+Space` | applications |
| `Super+Tab` | windows |
| `Super+a` | quick settings |
| `Print` / `Super+Shift+s` | Flameshot screenshot |
| `Super+Shift+w` | next wallpaper in `~/walls` |
| `Super+Return` | Alacritty |
| `Super+e` | Thunar |
| `Super+b` | Firefox |
| `Super+Escape` | power menu |
| `Super+1…5` | change workspace |
| `Super+Shift+1…5` | move window and follow |
| `Super+h/j/k/l` | focus |
| `Super+Shift+h/j/k/l` | move window |
| `Super+Ctrl+h/l` | shrink/grow the main pane |

## Bar controls

- Click the media title to play/pause; scroll it for previous/next.
- Scroll the volume or brightness bar to adjust it.
- Left-click Wi-Fi or Bluetooth to open its manager.
- Right-click Wi-Fi or Bluetooth to toggle the radio.

Display and wallpaper values live in `.config/qtile/defaults.py`. Validate
changes with `qtile check -c ~/.config/qtile/config.py`.
