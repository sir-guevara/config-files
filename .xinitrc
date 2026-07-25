#!/bin/sh

export GTK_THEME=Gruvbox-Dark-BL
export XCURSOR_THEME=Adwaita
export XCURSOR_SIZE=24

xsetroot -cursor_name left_ptr
exec dbus-launch --exit-with-session qtile start
