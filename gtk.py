import tkinter as tk

from gsnake import SnakeGame
from gdir import Directions


class GameRenderer:
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
            root, width=size.x, height=size.y, bg="blue")
        canvas.pack()
        root.bind("<Key>", lambda e: self.keyPress(e))

    def keyPress(self, e):
        key = e.keysym
        game = self._game

        if key == 'w' or key == 'Up':
            game.setDir(Directions.UP)

        if key == 'a' or key == 'Left':
            game.setDir(Directions.LEFT)

        if key == 'd' or key == 'Right':
            game.setDir(Directions.RIGHT)

        if key == 's' or key == 'Down':
            game.setDir(Directions.BOTTOM)

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
                fill = "green"

                if val > 0:
                    fill="white"
                
                if val == game._score:
                    fill="green"

                if val < 0:
                    fill="red"


                if val != 0:
                    canvas.create_rectangle(x, y, x+size, y+size, fill=fill)


                x += size

            y += size
