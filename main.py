import tkinter as tk
import sys
import time

from gvec import Vec2
from gdir import Directions
from gsnake import SnakeGame
from gtk import GameRenderer
import threading

game = SnakeGame(20, 20, 5)
game.pushApple()
game.pushSnake()

render = GameRenderer(game)
render.render()
render.mainloop()

# score = 3


# 0 0 4 3 2 1 0 0 0