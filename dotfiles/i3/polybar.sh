#!/usr/bin/env sh

# Used to launch the polybar from the i3config file!

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

for m in $(polybar --list-monitors | cut -d":" -f1); do
    echo "Setting up ${m}...";
    MONITOR=$m polybar -c ~/.config/polybar/config.ini  main &
done

# if type "xrandr"; then
#   for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
#     MONITOR=$m polybar -c ~/.config/polybar/config.ini main &
#   done
# else
#   polybar -c ~/.config/polybar/config.ini main &
# fi


# Launch polybar
# polybar main -c ~/.config/polybar/config &
# polybar top &
