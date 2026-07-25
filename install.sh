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

find "$repo_dir/.config" -type f ! -path '*/__pycache__/*' | while IFS= read -r source; do
    relative=${source#"$repo_dir/"}
    link_file "$source" "$HOME/$relative"
done

link_file "$repo_dir/.xinitrc" "$HOME/.xinitrc"
