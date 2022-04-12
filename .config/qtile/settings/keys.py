
### QTILE KEYS ###

from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
alt = "mod1"
myTerm = "alacritty" 
myBrowser = "brave"
myFileExplorer = "nemo"
myMenu = "rofi -show drun"

keys = [

    ### PROGRAMS ###

    # Terminal
    Key([mod], "Return", lazy.spawn(myTerm)),

    # Browser
    Key([mod], "b", lazy.spawn(myBrowser)),

    # File Explorer
    Key([mod], "e", lazy.spawn(myFileExplorer)),

    # Menu
    Key([mod], "m", lazy.spawn(myMenu)),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # GIMP
    Key([mod], "g", lazy.spawn("gimp")),

    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 3500")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),

    ### THEME CHANGER ###

    # MonokaiPro
    Key([mod, alt], "1",
    	lazy.spawn("nitrogen --set-zoom-fill --random --save"),
    	lazy.spawn("cp /home/(user)/.config/qtile/themes/MonokaiPro/colors.py /home/(user)/.config/qtile/themes"),
        lazy.restart(),
    	),

    # MaterialOcean
    Key([mod, alt], "2",
        lazy.spawn("nitrogen --set-zoom-fill --save /home/(user)/Imágenes/Wallpapers/SweetArch.png"),
    	lazy.spawn("cp /home/(user)/.config/qtile/themes/MaterialOcean/colors.py /home/(user)/.config/qtile/themes"),
        lazy.restart(),
        ),

    # Rosepine
    Key([mod, alt], "3",
    	lazy.spawn("nitrogen --set-zoom-fill --random --save"),
    	lazy.spawn("cp /home/(user)/.config/qtile/themes/Rosepine/colors.py /home/(user)/.config/qtile/themes"),
        lazy.restart(),
    	),

    # DarkGrey
    Key([mod, alt], "4",
    	lazy.spawn("nitrogen --set-zoom-fill --random --save"),
    	lazy.spawn("cp /home/(user)/.config/qtile/themes/DarkGrey//colors.py /home/(user)/.config/qtile/themes"),
        lazy.restart(),
    	),
 
    # Wallpaper Changer
    Key([mod], "w", lazy.spawn("nitrogen --set-zoom-fill --save --random")),

    ### Hardware ###

    # Volume
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pamixer --increase 5"),
        lazy.spawn("bash /home/(user)/.local/bin/volume/volume_increase.sh")
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pamixer --decrease 5"),
        lazy.spawn("bash /home/(user)/.local/bin/volume/volume_decrease.sh")
        ),
    Key([], "XF86AudioMute",
        lazy.spawn("pamixer --toggle-mute"),
        lazy.spawn("bash /home/(user)/.local/bin/volume/volume_mute.sh")
        ),
    
    # Brightness
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),
        lazy.spawn("bash /home/(user)/.local/bin/brightness/brightness_up.sh")
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        lazy.spawn("bash /home/(user)/.local/bin/brightness/brightness_down.sh")
        ),

    # Multimedia
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    ### HARDWARE KEYS (KEYBOARD) ###
    
    # Volume
    Key([alt], "F11",
        lazy.spawn("pamixer --increase 5"),
        lazy.spawn("bash /home/(user)/.local/bin/volume/volume_increase.sh")
        ),
    Key([alt], "F9",
        lazy.spawn("pamixer --decrease 5"),
        lazy.spawn("bash /home/(user)/.local/bin/volume/volume_decrease.sh")
        ),
    Key([alt], "F10",
        lazy.spawn("pamixer --toggle-mute"),
        lazy.spawn(" bash /home/(user)/.local/bin/volume/volume_mute.sh")
        ),
    
    # Brightness
    Key([alt], "F4",
        lazy.spawn("brightnessctl set +5%"),
        lazy.spawn("bash /home/(user)/.local/bin/brightness/brightness_up.sh")
        ),
    Key([alt], "F3",
        lazy.spawn("brightnessctl set 5%-"),
        lazy.spawn("bash /home/(user)/.local/bin/brightness/brightness_down.sh")
        ),
    
    # Multimedia
    Key([alt], "F8", lazy.spawn("playerctl next")),
    Key([alt], "F5", lazy.spawn("playerctl previous")),
    Key([alt], "F6", lazy.spawn("playerctl play")),

    ### WINDOW CONFIGS ###

    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    # Move windows between left/right
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    # Toggle between different layouts
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
]
