from talon.voice import Word, Context, Key, Rep, Str, press
import string

custom = Context('custom_input')
keymap = {}

keymap.update({
    #Quality of life
    'undo':Key('cmd-z'),
    'Find':Key('cmd-f'),
    'Find next':Key('cmd-g'),
    'copy':Key('cmd-c'),
    'Paste':Key('cmd-v'),
    '(wobble | woddle | waddle)': Key('alt-backspace'),
    'clap':Key('cmd-tab'),
    'smack':Key('ctrl-tab'),
    'black':Key('ctrl-shift-tab'),
    #Terminal goodies
    '(new directory | make directory)':'mkdir ',
    'npm':'npm ',
    'install':'install ',
    'pie': 'py',
    'sale':Key('shift-g'),
    #jupyter
    'running':Key('shift-enter'),

    #Words
    'grip':'grep',
    'rit':'reddit',
    '(tmax | teamx)':'tmux ', 
    '(pipe on | pipe gone)':'python',
    '(of cerium | a theoryvim | theoryvim)':'ethereum',
    'jupiter':'jupyter',
    #Chrome
    'chroma':Key('cmd-['),
    'chromed':Key('cmd-]'),

})
custom.keymap(keymap)
