#!/bin/sh
set -eu

# GDM requires GNOME Shell. Install a lightweight login manager first so the
# machine still reaches a graphical Qtile login after GNOME is removed.
sudo dnf install -y lightdm lightdm-gtk
sudo systemctl disable gdm.service
sudo systemctl enable --force lightdm.service

sudo dnf --setopt=protected_packages= remove -y \
    baobab \
    evolution-data-server \
    evolution-ews-core \
    gnome-backgrounds \
    gnome-boxes \
    gnome-browser-connector \
    gnome-calculator \
    gnome-calendar \
    gnome-characters \
    gnome-classic-session \
    gnome-clocks \
    gnome-color-manager \
    gnome-connections \
    gnome-contacts \
    gnome-control-center \
    gnome-disk-utility \
    gnome-font-viewer \
    gnome-initial-setup \
    gnome-logs \
    gnome-maps \
    gnome-remote-desktop \
    gnome-session-wayland-session \
    gnome-shell \
    gnome-shell-extension-apps-menu \
    gnome-shell-extension-background-logo \
    gnome-shell-extension-launch-new-instance \
    gnome-shell-extension-places-menu \
    gnome-shell-extension-window-list \
    gnome-software \
    gnome-system-monitor \
    gnome-text-editor \
    gnome-tour \
    gnome-user-docs \
    gnome-user-share \
    gnome-weather \
    nautilus \
    nautilus-python \
    simple-scan \
    yelp

printf '\nGNOME removed. LightDM will provide the next Qtile login. Reboot when ready.\n'
