import tkinter as tk
import sys
import time

from gvec import Vec2
from gdir import Directions
from gsnake import SnakeGame
from gtk import GameRenderer
import threading

game = SnakeGame(20, 20, 7)
render = GameRenderer(game)
game.pushSnake()
render.render()
render.mainloop()