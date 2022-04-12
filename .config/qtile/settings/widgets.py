
### QTILE WIDGETS ###

from libqtile import qtile
from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from .keys import myTerm
from themes.colors import colors


widget_defaults = dict(
    font = "UbuntuMono Nerd Font Bold",
    fontsize = 14,
    padding = 2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
        widget.GroupBox(
            fontsize = 12,
            font = "Ubuntu Bold",
            active = colors[2],
            inactive = colors[1],
            highlight_method = 'block',
            urgent_alert_method = "block",
            urgent_border = colors[6],
            this_current_screen_border = colors[4],
            this_screen_border = colors[1],
            other_current_screen_border = colors[1],
            other_screen_border = colors[0],
            rounded = False,
            margin_x = 0,
            margin_y = 3,
            padding_y = 8,
            padding_x = 4,
            ),
        widget.Sep(
            padding = 5,
            foreground = colors[0],
            background = colors[0],
            ),
        widget.WindowName(
            font = "Ubuntu Bold",
            fontsize = 0,
            foreground = colors[4],
            max_chars = 70,
            ),
        widget.TextBox(
            "",
            fontsize = 44,
            foreground = colors[11],
            padding = -3,
            ),
        widget.TextBox(
            " ",
            fontsize = 16,
            background = colors[11],
            foreground = colors[3],
            ),
        widget.TextBox(
            "ArchLinux ",
            background = colors[11],
            foreground = colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
            ),
        widget.TextBox(
            "",
            fontsize = 44,
            padding = -3,
            background = colors[11],
            foreground = colors[10],
            ),
        widget.TextBox(
            " ",
            fontsize = 16,
            background = colors[10],
            foreground = colors[3],
            ),
        widget.TextBox(
            "Qtile ",
            background = colors[10],
            foreground = colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e nvim /home/dilan/.config/qtile/settings/keys.py')},
            ),
        widget.TextBox(
            "",
            fontsize = 44,
            foreground = colors[9],
            background = colors[10],
            padding = -3,
            ),
       widget.CurrentLayoutIcon(
            background = colors[9],
            scale = 0.60,
            ),
       widget.CurrentLayout(
            background = colors[9],
            foreground = colors[3],
            ),
       widget.Sep(
            foreground = colors[9],
            background = colors[9],
            padding = 4,
            ),
       widget.TextBox(
            "",
            fontsize = 44,
            foreground = colors[8],
            background = colors[9],
            padding = -3,
            ),
        widget.Clock(
            foreground = colors[3],
            background = colors[8],
            format="  %d/%m/%Y   %I:%M %p ",
            ),
        widget.TextBox(
            "",
            fontsize = 44,
            foreground = colors[0],
            background = colors[8],
            padding = -3,
            ),
        widget.Systray(
            background = colors[0],
            padding = 4,
            ),
            ],
        31,
        background = colors[0],
        margin = 4,
        opacity = 0.95,
        ),
        ),
        ]
