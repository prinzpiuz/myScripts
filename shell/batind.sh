#!/bin/bash
export DISPLAY=:0
state=$(upower -i $(upower -e | grep BAT) | grep --color=never -E "state" )
stat=${state:25:32}
batperct=$(upower -i $(upower -e | grep '/battery') | grep  -E "percentage:")
bat=${batperct:24:26}
intbat=$(echo $bat | cut -d'%' -f1)
if [ "$intbat" -lt "15" -a "$stat" == "discharging" ]; then
    notify-send 'battery low..! please plugin charger..... charge is only' "$intbat"    
fi   


