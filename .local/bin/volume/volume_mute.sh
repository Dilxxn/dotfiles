#!/bin/bash

volume=$(pamixer --get-volume)
dunstify -u low -r 888 -h int:value:0 --icon=~/.local/icons/sound_mute.png "Volumen: 0%" -t 1500
