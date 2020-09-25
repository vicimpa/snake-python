from gmap import GameMap
from gvec import Vec2
from gdir import Directions
from random import randint


class SnakeGame:
    def __init__(self, width=10, height=10, score=4):
        self._map = GameMap(width, height)
        self._score = score
        self._dir = Directions.randomValue()
        self._prevDir = self._dir.clone()

    def setDir(self, dir: Directions):
        val = dir.value.clone()

        if val.mul(-1).notEqually(self._prevDir):
            self._dir = dir.value

    def getSize(self):
        return self._map.getSize()

    def pushSnake(self):
        map = self._map

        centerScore = int(self._score / 2)

        center = map.getSize()
        center.div(2)

        for s in range(self._score, 0, -1):
            centerCopy = center.clone()
            delta = self._dir.clone()
            delta.mul(-1 * (s - centerScore))
            centerCopy.min(delta)
            map.setValueOfPosition(centerCopy, s)

    def splitSnake(self, score): 
        map = self._map

        change = []

        for x in range(self._score, 0, -1):
            pos = map.getIndexOfValue(x)
            val = x - score

            if val <= 0:
                val = -1

            change.append([pos, val])

        for c in change:
            map.setValueOfIndex(c[0], c[1])

        self._score -= score


    def loop(self, score=None, newPosition=None):
        map = self._map

        if score is None:
            score = self._score

        if score == self._score:
            self._prevDir = self._dir

        nowPosition = map.getPositionOfValue(score)

        if newPosition is None:
            newPosition = nowPosition.clone().add(self._dir)
            
            if newPosition.x < 0:
                newPosition.x += map._width

            if newPosition.x > map._width - 1:
                newPosition.x -= map._width
            
            if newPosition.y < 0:
                newPosition.y += map._width

            if newPosition.y > map._height - 1:
                newPosition.y -= map._height

        if score == self._score:
            newVal = map.getValueOfPosition(newPosition)

            if newVal > 0:
                self.splitSnake(newVal)
                return self.loop()

            if newVal < 0:
                self._score += 1
                map.setValueOfPosition(newPosition, self._score)

                if map.getCountOfValue(-1) == 0:
                    self.pushApple()
                    
                return

        map.moveValueOfPosition(nowPosition, newPosition)

        if score > 0:
            self.loop(score-1, nowPosition)

    def pushApple(self):
        map = self._map

        pos = []

        for i in range(map._size):
            val = map.getValueOfIndex(i)

            if val == 0:
                pos.append(i)


        rand = randint(0, len(pos) - 1)
        map.setValueOfIndex(pos[rand], -1)
        

    def getRenderMap(self):
        outRender = []
        map = self._map

        for y in range(0, map._height):
            row = []

            for x in range(0, map._width):
                vec = Vec2(x, y)
                ind = map.getIndexOfPosition(vec)
                val = map.getValueOfIndex(ind)
                row.append(val)

            outRender.append(row)

        return outRender
