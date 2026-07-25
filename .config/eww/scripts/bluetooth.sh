#!/bin/sh

#
# FreeBSD Bluetooth Controller
#

status() {

    if service bluetooth status 2>/dev/null | grep -q "is running"; then
        echo "On"
    else
        echo "Off"
    fi

}

toggle() {

    if service bluetooth status 2>/dev/null | grep -q "is running"; then
        doas service bluetooth stop >/dev/null
    else
        doas service bluetooth start >/dev/null
    fi

}

case "$1" in

status)
    status
    ;;

toggle)
    toggle
    ;;

*)
    echo "Usage:"
    echo "bluetooth.sh status"
    echo "bluetooth.sh toggle"
    exit 1
    ;;

esac