#!/bin/bash

pamixer -u
volume=$(pamixer --get-volume)
dunstify -u low -r 888 -h int:value:"$volume" --icon=~/.local/icons/sound_down.png "Volumen: ${volume}%" -t 1500
