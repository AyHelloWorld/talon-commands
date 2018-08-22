from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ctrl, app
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string
mapping = {
'semicolon': ';',
'new-line': '\n',
'new-paragraph': '\n\n',
}

def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def text(m):
    tmp = [str(s).lower() for s in m.dgndictation[0]._words]
    words = [parse_word(word) for word in tmp]
    Str(' '.join(words))(None)


#Creating a toggle 4 normal speech, 2 code
def codeOn(m):
    sentence.unload()
    ctn.load()
    app.notify('Code on: ')
def codeOff(m):
    sentence.load()
    ctn.unload()
    app.notify('Code off: ')
ctc= Context('sentenceControl')

ctc.keymap({
    'code on':codeOn,
    'code off':codeOff,
 })
sentence= Context('sentence')

sentence.keymap({
    '<dgndictation> [over]': [text, ' '],

 }) 
ctn = Context('code')
ctn.keymap(dict([(str(i), str(i)) for i in range(0, 10)])
)
