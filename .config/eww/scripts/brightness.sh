#!/bin/sh

# FreeBSD backlight controller for Eww.
#
# Usage:
#   brightness.sh get
#   brightness.sh set 50
#   brightness.sh up
#   brightness.sh down

BACKLIGHT_DEVICE="/dev/backlight/backlight0"

get_brightness() {
    value="$(
        backlight -f "$BACKLIGHT_DEVICE" 2>/dev/null |
            awk '
                {
                    for (i = 1; i <= NF; i++) {
                        if ($i ~ /^[0-9]+(\.[0-9]+)?$/) {
                            printf "%d\n", $i
                            exit
                        }
                    }
                }
            '
    )"

    case "$value" in
        ''|*[!0-9]*)
            echo 50
            ;;
        *)
            echo "$value"
            ;;
    esac
}

set_brightness() {
    value="${1%%.*}"

    case "$value" in
        ''|*[!0-9]*)
            exit 1
            ;;
    esac

    if [ "$value" -lt 5 ]; then
        value=5
    elif [ "$value" -gt 100 ]; then
        value=100
    fi

    backlight -f "$BACKLIGHT_DEVICE" "$value"
}

case "$1" in
    get)
        get_brightness
        ;;

    set)
        set_brightness "$2"
        ;;

    up)
        backlight -f "$BACKLIGHT_DEVICE" incr 5
        ;;

    down)
        current="$(get_brightness)"

        if [ "$current" -le 5 ]; then
            backlight -f "$BACKLIGHT_DEVICE" 5
        else
            backlight -f "$BACKLIGHT_DEVICE" decr 5
        fi
        ;;

    *)
        echo "Usage: $0 {get|set VALUE|up|down}" >&2
        exit 1
        ;;
esac