
class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.height * self.width

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def printInfo(self):
        print("width:{0} height:{1} area:{2} perimeter:{3}".format(self.width,self.height,self.getArea(),self.getPerimeter()))


R1 = Rectangle(4, 10)
R2 = Rectangle(3.5, 35.7)

R1.printInfo()
R2.printInfo()



