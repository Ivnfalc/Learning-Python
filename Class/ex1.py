class Line:

    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def distancia(self):
        x1,y1 = self.c1
        x2,y2 = self.c2

        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    def slp(self):
        x1, y1 = self.c1
        x2, y2 = self.c2
        return (y1-y2) / (x1-x2)

line = Line ((2,4) , (6,10))
print(line.distancia())
print(line.slp())