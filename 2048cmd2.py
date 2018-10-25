from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl

from Game2048 import Game

buffer = Buffer()

bindings = KeyBindings()
game = Game(tips = "",
    end="游戏结束。你获得的分数是{},请按r或者回车退出"
)

root_container = HSplit([
    Window(content = BufferControl(buffer = buffer)),
    Window(content = FormattedTextControl(text="wasd或上下左右建移动,r重新开始，esc退出"))
])

length = 0
def refresh():
    global buffer,length
    buffer.reset()
    length = len(game.content())
    buffer.insert_text(game.content())

@bindings.add('w')
@bindings.add('up')
def _(event):
    game.up()
    game.generate()
    refresh()

@bindings.add('a')
@bindings.add('left')
def _(event):
    game.left()
    game.generate()
    refresh()

@bindings.add('s')
@bindings.add('down')
def _(event):
    game.down()
    game.generate()
    refresh()

@bindings.add('d')
@bindings.add('right')
def _(event):
    game.right()
    game.generate()
    refresh()

@bindings.add('r')
def _(event):
    game.init()
    refresh()

@bindings.add('escape')
@bindings.add('q')
def _(event):
    game.end()
    refresh()
    event.app.exit()

@bindings.add('<any>')
def _(event):
    game.isEND()
    if game.Flag == game.END:
        game.end()

refresh()
layout = Layout(root_container)
app = Application(layout=layout, key_bindings=bindings)
app.run()