#!/bin/sh

# ~/.screenlayout/default_screenlayout.sh

# Use arandr to create the script! If it is not there, the Xserver will complain


xrandr --output USB-C-0 --off --output HDMI-0 --off --output DP-5 --off --output DP-4 --off --output DP-3 --off --output DP-2 --primary --mode 3840x2160 --pos 0x0 --rotate normal --output DP-1 --off --output DP-0 --mode 3840x2160 --pos 3840x0 --rotate normal
