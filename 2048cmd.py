from prompt_toolkit import prompt
# from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from Game2048 import Game

bindings = KeyBindings()
game = Game(tips="wasd或上下左右建移动,r重新开始，回车退出",
    end="游戏结束。你获得的分数是{},请按r或者回车退出"
)

@bindings.add('w')
@bindings.add('up')
def _(event):
    game.up()
    game.generate()
    game.show()

@bindings.add('a')
@bindings.add('left')
def _(event):
    game.left()
    game.generate()
    game.show()

@bindings.add('s')
@bindings.add('down')
def _(event):
    game.down()
    game.generate()
    game.show()

@bindings.add('d')
@bindings.add('right')
def _(event):
    game.right()
    game.generate()
    game.show()

@bindings.add('r')
def _(event):
    game.init()
    game.show()

@bindings.add('<any>')
def _(event):
    game.isEND()
    if game.Flag == game.END:
        game.end()


def main():
    game.init()
    game.show()
    prompt("", key_bindings=bindings)
    game.end()
    print("\nWelcome To UCE!")

if __name__ == '__main__':
    main()