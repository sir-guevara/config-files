#!/bin/sh

#
# FreeBSD Wi-Fi Controller
#
# Usage:
#
# network.sh status
# network.sh ssid
# network.sh toggle
#

INTERFACE="$(ifconfig -l | tr ' ' '\n' | grep -E '^(wlan|iwl|ath|urtwn|run|rtwn)' | head -1)"

if [ -z "$INTERFACE" ]; then
    exit 1
fi


status() {
    if ifconfig "$INTERFACE" | grep -q "status: associated"; then
        echo "Connected"
    else
        echo "Disconnected"
    fi
}


ssid() {
    SSID="$(
        wpa_cli -i "$INTERFACE" status 2>/dev/null |
            awk -F= '$1 == "ssid" {
                print substr($0, index($0, "=") + 1)
                exit
            }'
    )"

    if [ -n "$SSID" ]; then
        echo "$SSID"
    else
        echo "Disconnected"
    fi
}

toggle() {

    if ifconfig "$INTERFACE" | grep -q "status: associated"; then
        doas ifconfig "$INTERFACE" down
    else
        doas ifconfig "$INTERFACE" up
    fi

}

case "$1" in

status)
    status
    ;;

ssid)
    ssid
    ;;

toggle)
    toggle
    ;;

*)
    echo "Usage:"
    echo "network.sh status"
    echo "network.sh ssid"
    echo "network.sh toggle"
    exit 1
    ;;

esac