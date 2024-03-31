class GeometircObject:
    def __init__(self, color="blue", filled=True):
        self.color = color
        self.filled = filled


class Triangle(GeometircObject):
    def __init__(self, side1=1, side2=1, side3=1):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getS1(self):
        return self.side1

    def getS2(self):
        return self.side2

    def getS3(self):
        return self.side3

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return "Triangle: side1 = " + str(self.side1) + "side2 = " + str(self.side2) + "side3 = " + str(self.side3)

    def printInfo(self):
        print("color:{0}, filled:{1}, area:{2}, perimeter:{3}".format(self.color, self.filled, self.getArea(),
                                                                      self.getPerimeter()))


t = Triangle(10, 20, 25)
t.filled = True
t.color = "yellow"
t.printInfo()
