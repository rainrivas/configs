#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

#polybar bar2 -c ~/configs/polybar/polybar.conf &
polybar topbar2 -c ~/configs/polybar/polybar.conf &

