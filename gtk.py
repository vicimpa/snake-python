import tkinter as tk
from tkinter.constants import NONE

from gsnake import SnakeGame
from gdir import Directions

keys = {
    'w': Directions.UP,
    'Up': Directions.UP,
    
    'a': Directions.LEFT,
    'Left': Directions.LEFT,

    'd': Directions.RIGHT,
    'Right': Directions.RIGHT,

    's': Directions.BOTTOM,
    'Down': Directions.BOTTOM
}

class GameRenderer:
    _colors=["cyan", "yellow", "magenta"]

    def __init__(self, game: SnakeGame, name="SnakeGame"):
        self._game = game
        self._work = False
        root = self._root = tk.Tk()
        root.title(name)
        sizeCol = self._size = 20
        size = game.getSize().mul(sizeCol)
        geometry = str(size.x+10)+'x'+str(size.y+10)
        root.geometry(geometry)
        canvas = self._canvas = tk.Canvas(
            root, width=size.x, height=size.y, bg="black")
        canvas.pack()
        root.bind("<Key>", lambda e: self.keyPress(e))

    def keyPress(self, e):
        key = e.keysym
        game = self._game
        dir = keys.get(key)

        if not dir is None:
            game.setDir(dir)

    def loop(self):
        root = self._root

        if self._work:
            game = self._game
            game.loop()
            self.render()
            root.after(200, self.loop)

    def mainloop(self):
        self._work = True
        self.loop()
        root = self._root
        root.mainloop()

    def getCurrentColor(self):
        return self._colors[self._game._score % len(self._colors)]

    def render(self):
        game = self._game
        canvas = self._canvas
        size = self._size

        canvas.delete("all")

        map = game.getRenderMap()

        y = 0

        for row in map:
            x = 0

            for val in row:
                if val > 0:
                    fill=self.getCurrentColor()
                
                if val == game._score:
                    fill="green"

                if val < 0:
                    fill="red"

                if val != 0:
                    canvas.create_rectangle(x, y, x+size, y+size, fill=fill)

                x += size

            y += size

        canvas.create_text(10, 10, text='Score: ' + str(game._score),fill="white", justify=tk.LEFT, anchor=tk.NW)