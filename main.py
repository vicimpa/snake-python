from gsnake import SnakeGame
from gtk import GameRenderer

game = SnakeGame(20, 20, 5)
game.pushSnake()
game.pushApple()

render = GameRenderer(game)
render.render()
render.mainloop()