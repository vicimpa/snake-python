class Vec2:
    def __str__(self):
        return 'Vec2(x: ' + str(self.x) + ', y: ' + str(self.y) + ')'

    def __init__(self, x: int = 0, y: int = 0):
        d = convertVec(x, y)

        self.x = d['x']
        self.y = d['y']

    def add(self, x, y=None):
        d = convertVec(x, y)

        self.x += d['x']
        self.y += d['y']

        return self

    def min(self, x, y=None):
        d = convertVec(x, y)

        self.x -= d['x']
        self.y -= d['y']

        return self

    def mul(self, x, y=None):
        d = convertVec(x, y)

        self.x *= d['x']
        self.y *= d['y']

        return self

    def div(self, x, y=None):
        d = convertVec(x, y)

        self.x /= d['x']
        self.y /= d['y']

        return self

    def equally(self, x, y=None):
        d = convertVec(x, y)

        if self.x != d['x']:
            return False

        if self.y != d['y']:
            return False

        return True
    
    def notEqually(self, x, y=None):
        if self.equally(x, y):
            return False
        else:
            return True

    def clone(self):
        return Vec2(self)

def convertVec(x=0, y=0):
    if isinstance(x, Vec2):
        y = x.y
        x = x.x

    if x is None:
        x = 0

    if y is None:
        y = x

    return {'x': x, 'y': y}
