#!/usr/bin/env bash

# https://thevaluable.dev/window-manager-mouseless-i3/
# Requires imagemagick and scrot

img=/tmp/i3lock.png

# Take a screenshot
scrot $img

# BLUR?
# -------------------------------------------------------------------------------- #
# convert $img -blur 0x20 $img

# PIXELATE?
# -------------------------------------------------------------------------------- #
# In order to maintain the image size, the upscaling of the downscaled image should be done by
# a factor of 1/(down_scale/100.0)*100
# e.g.
#   - downscale by x = 10%
#   -   upscale by y = 1/(x/100.0)*100 = 1000%
convert $img -scale 2% -scale 5000% $img


i3lock --image=$img --ignore-empty-password
