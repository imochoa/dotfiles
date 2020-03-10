#!/usr/bin/env bash

# https://thevaluable.dev/window-manager-mouseless-i3/
# Requires imagemagick and scrot

img=/tmp/i3lock.png

scrot $img

# In order to maintain the image size, the upscaling of the downscaled image should be done by
# a factor of 1/(down_scale/100.0)*100
# e.g.
#   - downscale by 10%
#   -   upscale by 1/(10/100.0)*100 = 1000%

convert $img -scale 5% -scale 2000% $img

i3lock --image=$img --ignore-empty-password
