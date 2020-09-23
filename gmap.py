from gvec import Vec2

class GameMap:
    def __init__(self, width: int = 10, height: int = 10):
        self._map = [0 for i in range(width * height)]
        self._width = width
        self._height = height
        self._size = width * height

    def getSize(self):
        return Vec2(self._width, self._height)

    def getValueOfIndex(self, index: int):
        return self._map[index]

    def setValueOfIndex(self, index: int, value: int):
        self._map[index] = value

    def getValueOfPosition(self, vec: Vec2):
        return self._map[self.getIndexOfPosition(vec)]

    def setValueOfPosition(self, vec: Vec2, value: int):
        self._map[self.getIndexOfPosition(vec)] = value

    def getIndexOfPosition(self, vec: Vec2):
        return int(vec.y * self._width + vec.x)

    def getPositionOfIndex(self, index: int):
        x: int = index % self._width
        y: int = (index - x) / self._height
        return Vec2(x, y)

    def getIndexOfValue(self, value: int):
        return self._map.index(value)

    def getPositionOfValue(self, value: int):
        return self.getPositionOfIndex(self.getIndexOfValue(value))

    def getCountOfValue(self, value: int):
        count = 0

        for i in range(self._size):
            if self._map[i] == value:
                count += 1

        return count

    def moveValueOfIndex(self, indexA: int, indexB: int):
        if indexA == indexB:
            return

        valueA = self._map[indexA]
        valueB = self._map[indexB]

        self._map[indexA] = valueB
        self._map[indexB] = valueA

    def moveValueOfPosition(self, vecA: Vec2, vecB: Vec2):
        indexA = self.getIndexOfPosition(vecA)
        indexB = self.getIndexOfPosition(vecB)

        self.moveValueOfIndex(indexA, indexB)