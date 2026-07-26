#!/bin/sh
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
theme=Gruvbox-B-MB-Light-Soft
icons=Gruvbox-Dark
desktop_user=${SUDO_USER:-${USER:-}}
desktop_home=$(getent passwd "$desktop_user" | cut -d: -f6)

if [ "$(id -u)" -ne 0 ]; then
    exec sudo "$0" "$@"
fi

install -d /usr/share/themes /usr/share/icons /usr/share/backgrounds /etc/lightdm
test -d "$desktop_home/.local/share/themes/$theme"
test -d "$desktop_home/.local/share/icons/$icons"
cp -a "$desktop_home/.local/share/themes/$theme" /usr/share/themes/
cp -a "$desktop_home/.local/share/icons/$icons" /usr/share/icons/
install -m 0644 "$desktop_home/walls/wall10.png" /usr/share/backgrounds/groovy-lightdm.jpg

if [ -f /etc/lightdm/lightdm-gtk-greeter.conf ] && \
   [ ! -f /etc/lightdm/lightdm-gtk-greeter.conf.groovy-backup ]; then
    cp -a /etc/lightdm/lightdm-gtk-greeter.conf \
        /etc/lightdm/lightdm-gtk-greeter.conf.groovy-backup
fi

install -m 0644 "$repo_dir/lightdm/lightdm-gtk-greeter.conf" \
    /etc/lightdm/lightdm-gtk-greeter.conf

printf '%s\n' 'Gruvbox LightDM theme installed.'
printf '%s\n' 'Fingerprint PAM is managed by Fedora authselect.'
printf '%s\n' 'Enroll another finger with: fprintd-enroll'
