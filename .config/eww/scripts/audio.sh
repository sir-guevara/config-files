#!/bin/sh

# Unified FreeBSD audio controller for Eww.
#
# Usage:
#   audio.sh get-volume
#   audio.sh set-volume 50
#   audio.sh get-mute
#   audio.sh toggle-mute
#   audio.sh mute
#   audio.sh unmute

get_volume() {
    mixer -o 2>/dev/null |
        awk -F'[=:]' '
            /^vol\.volume=/ {
                printf "%.0f\n", $2 * 100
                exit
            }
        '
}

set_volume() {
    value="${1%%.*}"

    case "$value" in
        ''|*[!0-9]*)
            exit 1
            ;;
    esac

    if [ "$value" -lt 0 ]; then
        value=0
    elif [ "$value" -gt 100 ]; then
        value=100
    fi

    decimal="$(awk -v value="$value" 'BEGIN { printf "%.2f", value / 100 }')"

    mixer "vol.volume=${decimal}:${decimal}" >/dev/null 2>&1
}

get_mute() {
    mute="$(
        mixer -o 2>/dev/null |
            awk -F= '
                /^vol\.mute=/ {
                    print $2
                    exit
                }
            '
    )"

    case "$mute" in
        on|1)
            echo true
            ;;
        *)
            echo false
            ;;
    esac
}

toggle_mute() {
    mixer "vol.mute=toggle" >/dev/null 2>&1
}

mute_audio() {
    mixer "vol.mute=on" >/dev/null 2>&1
}

unmute_audio() {
    mixer "vol.mute=off" >/dev/null 2>&1
}

case "$1" in
    get-volume)
        get_volume
        ;;

    set-volume)
        set_volume "$2"
        ;;

    get-mute)
        get_mute
        ;;

    toggle-mute)
        toggle_mute
        ;;

    mute)
        mute_audio
        ;;

    unmute)
        unmute_audio
        ;;

    *)
        echo "Usage: $0 {get-volume|set-volume VALUE|get-mute|toggle-mute|mute|unmute}" >&2
        exit 1
        ;;
esac