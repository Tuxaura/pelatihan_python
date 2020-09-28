class Point:

    sumbu = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def reset(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Titik nya ({self.x}, {self.y})")


poin = Point(3, 2)

poin.draw()
poin = Point.reset()
poin.draw()
