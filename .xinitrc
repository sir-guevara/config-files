#!/bin/sh

export XCURSOR_THEME=Adwaita
export XCURSOR_SIZE=24

# Keep GTK4/libadwaita and applications using the desktop portal in dark mode.
gsettings set org.gnome.desktop.interface color-scheme prefer-dark 2>/dev/null || true
gsettings set org.gnome.desktop.interface gtk-theme Nordic-darker-standard-buttons 2>/dev/null || true
gsettings set org.gnome.desktop.interface icon-theme Papirus-Dark 2>/dev/null || true

xsetroot -cursor_name left_ptr
exec dbus-launch --exit-with-session qtile start
