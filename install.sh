#!/bin/sh
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
timestamp=$(date +%Y%m%d-%H%M%S)

link_file() {
    source=$1
    destination=$2
    mkdir -p "$(dirname -- "$destination")"

    if [ -e "$destination" ] && [ ! -L "$destination" ]; then
        mv "$destination" "${destination}.backup-${timestamp}"
    else
        rm -f "$destination"
    fi

    ln -s "$source" "$destination"
    printf 'linked %s -> %s\n' "$destination" "$source"
}

remove_legacy_link() {
    destination=$1

    if [ -L "$destination" ]; then
        target=$(readlink "$destination")
        case "$target" in
            "$repo_dir"/*)
                rm -f "$destination"
                printf 'removed obsolete link %s\n' "$destination"
                ;;
        esac
    fi
}

link_mozilla_theme() {
    profiles_file=$1
    profiles_root=${profiles_file%/*}

    [ -f "$profiles_file" ] || return 0

    sed -n 's/^Path=//p' "$profiles_file" | while IFS= read -r profile; do
        case "$profile" in
            /*) profile_dir=$profile ;;
            *) profile_dir=$profiles_root/$profile ;;
        esac

        [ -d "$profile_dir" ] || continue
        link_file "$repo_dir/.config/mozilla-gruvbox/userChrome.css" \
            "$profile_dir/chrome/userChrome.css"
        link_file "$repo_dir/.config/mozilla-gruvbox/userContent.css" \
            "$profile_dir/chrome/userContent.css"
        link_file "$repo_dir/.config/mozilla-gruvbox/user.js" \
            "$profile_dir/user.js"
    done
}

for legacy in \
    "$HOME/.config/kitty/kitty.conf" \
    "$HOME/.config/picom/picom.conf" \
    "$HOME/.config/dunst/dunstrc" \
    "$HOME/.config/eww/eww.scss" \
    "$HOME/.config/eww/eww.yuck"
do
    remove_legacy_link "$legacy"
done

find "$repo_dir/.config" -type f ! -path '*/__pycache__/*' | while IFS= read -r source; do
    relative=${source#"$repo_dir/"}
    link_file "$source" "$HOME/$relative"
done

find "$repo_dir/.local" -type f ! -path '*/__pycache__/*' | while IFS= read -r source; do
    relative=${source#"$repo_dir/"}
    link_file "$source" "$HOME/$relative"
done

link_file "$repo_dir/.xinitrc" "$HOME/.xinitrc"

link_mozilla_theme "$HOME/.mozilla/firefox/profiles.ini"
link_mozilla_theme "$HOME/.thunderbird/profiles.ini"
