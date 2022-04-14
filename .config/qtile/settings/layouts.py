### LAYOUTS ###

from libqtile.config import Match
from libqtile import layout
from themes.colors import colors

layout_theme = {"border_width": 1, 
                "margin": 4,
                "border_focus": colors[4],
                "border_normal": colors[0],
                }

layouts = [
    layout.Columns(
        **layout_theme,
        border_on_single = True,
        margin_on_single = 4,
        ),
    layout.Max(),
    layout.Floating(
        **layout_theme,
        ),
    ]
 
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
    border_focus = colors[4],
    border_width = 2,
)
