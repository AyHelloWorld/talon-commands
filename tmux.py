from talon.voice import Word, Context, Key, Rep, Str, press
import string

ctx = Context('tmux', bundle='com.apple.Terminal', func=lambda app, win: 'tmux' in win.title)
keymap = {}

keymap.update({
#   '':Key('ctrl-n'),
   'lastly':Key('ctrl-p'),
   'wendy':Key('ctrl-b'),
})
ctx.keymap(keymap)
