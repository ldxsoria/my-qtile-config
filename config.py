from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#Startup
import os
import subprocess

#Startup, esto hace que ejecute los programas que estan en autostart.sh
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

mod = "mod4"
terminal = guess_terminal()
colorBarra="#4B4847.0"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    #Teclas para menu Rofi
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Abrir menu"),

    #Ejecutar navegador
    Key([mod], "c", lazy.spawn("google-chrome-stable"), desc="Abrir Chrome"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Abrir Firefox"),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    #Key([mod], "Return", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #Control de Volumen
    #Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SKIN@ -5%")),
    #Key([mod], "F2", lazy.spawn("amixer set Master 5%- unmute")),
    #Key([mod], "F3", lazy.spawn("amixer set Master 5%+ unmute")),
    #Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer set Master 5%+ unmute')),
    #Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer set Master 5%-  unmute')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pactl -- set-sink-volume @DEFAULT_SINK@ -5%')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pactl -- set-sink-volume @DEFAULT_SINK@ +5%')),
    Key([], 'XF86AudioMute', lazy.spawn('pactl -- set-sink-mute @DEFAULT_SINK@ toggle')),
    Key([mod], 'F2', lazy.spawn('pactl -- set-sink-volume @DEFAULT_SINK@ -5%')),
    Key([mod], 'F3', lazy.spawn('pactl -- set-sink-volume @DEFAULT_SINK@ +5%')),
    Key([mod], 'F1', lazy.spawn('pactl -- set-sink-mute @DEFAULT_SINK@ toggle')),
    #Key([], 'XF86AudioMute', lazy.spawn('amixer set Master toggle')),

    #Brillo
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +10%')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 10%-')),

    #Caputra de pantalla
    Key([mod], "0", lazy.spawn("scrot")),
    Key([mod, "control"], "0", lazy.spawn("scrot -s")),

]

#Listado de iconos nerd fonts: https://www.nerdfonts.com/cheat-sheet
#1 - nf-linux-archlinux
#2 - nf-fa-firefox
#3 - nf-dev-terminal
#7 - nf-fa-desktop
#4 - nf-custom-folder_open
#5 - nf-fa-file_code_o
#6 - nf-mdi-music_box_outline
#8 - nf-fa-hashtag

groups = [Group(i) for i in [
    " ??? "," ??? "," ??? "," ??? "," ??? "," ??? "," ??? "," ??? "
]]

for i, group in enumerate(groups):
    numeroEscritorio=str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], numeroEscritorio, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], numeroEscritorio, lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    #layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=2),
    layout.Columns(border_focus_stack=['#d75f5f', '#ffffff'], border_width=2),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Ubuntu Mono Nerd Fonts',
    fontsize=18,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                        #'launch': ("#ffffff", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M:%S %p'),
                widget.QuickExit(),
                widget.CurrentLayout(),
            ],
            40,
            background=colorBarra,
            # opacity=0.2,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
        Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                #widget.QuickExit(),
                widget.CurrentLayout(),
            ],
            34,
            background=colorBarra,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

