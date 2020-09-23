from enum import Enum
from gvec import Vec2
from random import randint

class Directions(Enum):
    UP = Vec2(0, -1)
    LEFT = Vec2(-1, 0)
    RIGHT = Vec2(1, 0)
    BOTTOM = Vec2(0, 1)

    @staticmethod
    def randomValue():
        directions = []

        for key in Directions:
            value = key.value
            directions.append(value)

        index = randint(0, len(directions) - 1)
        return Vec2(directions[index])