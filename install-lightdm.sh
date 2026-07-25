#!/bin/sh
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
source_config="$repo_dir/lightdm/lightdm-gtk-greeter.conf"
prefix=${PREFIX:-/usr/local}
config_dir=${LIGHTDM_CONFIG_DIR:-"$prefix/etc/lightdm"}
share_dir=${LIGHTDM_SHARE_DIR:-"$prefix/share/backgrounds"}
destination="$config_dir/lightdm-gtk-greeter.conf"
wallpaper=${1:-}
timestamp=$(date +%Y%m%d-%H%M%S)

if [ "$(id -u)" -ne 0 ]; then
    printf 'Run this system installer as root, for example:\n' >&2
    printf '  doas %s [wallpaper]\n' "$0" >&2
    exit 1
fi

mkdir -p "$config_dir"
if [ -f "$destination" ]; then
    cp -p "$destination" "${destination}.backup-${timestamp}"
fi
cp "$source_config" "$destination"

if [ -n "$wallpaper" ]; then
    if [ ! -f "$wallpaper" ]; then
        printf 'Wallpaper not found: %s\n' "$wallpaper" >&2
        exit 1
    fi

    mkdir -p "$share_dir"
    filename=${wallpaper##*/}
    case "$filename" in
        *.*) extension=.${filename##*.} ;;
        *) extension= ;;
    esac
    installed_wallpaper="$share_dir/gruvbox-login$extension"
    cp "$wallpaper" "$installed_wallpaper"
    chmod 0644 "$installed_wallpaper"
    temporary_config="${destination}.tmp.$$"
    awk -v background="$installed_wallpaper" '
        /^background = / { print "background = " background; next }
        { print }
    ' "$destination" > "$temporary_config"
    mv "$temporary_config" "$destination"
fi

chmod 0644 "$destination"
printf 'Installed %s\n' "$destination"
printf '%s\n' 'Restart LightDM to apply the greeter theme.'
