
### QTILE GROUPS ###

from libqtile.config import Group, Key
from libqtile.lazy import lazy
from .keys import mod, keys

groups = [Group(i) for i in [
    "NET", "SYS", "DEV", "MDA", "FLS", "MSC", "IMG", "DOC", "GFX",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
