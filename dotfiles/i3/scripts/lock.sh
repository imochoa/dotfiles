#!/usr/bin/env bash

# https://thevaluable.dev/window-manager-mouseless-i3/
# Requires imagemagick and scrot

img=/tmp/i3lock.png

scrot $img
convert $img -scale 10% -scale 1000% $img

i3lock --image=$img --ignore-empty-password
