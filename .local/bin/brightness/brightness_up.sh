
#!/bin/bash

brightness=$(light -G)
dunstify -u low -r 888 -h int:value:"$brightness" --icon=~/.local/icons/light.png "Brillo: ${brightness}%" -t 1500
