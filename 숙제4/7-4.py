
SLOW = 1
MEDIUM = 2
FAST = 3


class Fan:
    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self.__speed = SLOW
        self.__on = on
        self.__radius = radius
        self.__color = color

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, s):
        self.__speed = s

    def getRadius(self):
        return self.__radius

    def setRadius(self, r):
        self.__radius = r

    def getColor(self):
        return self.__color

    def setColor(self, c):
        self.__color = c

    def getOn(self):
        return self.__on

    def setOn(self, o):
        self.__on = o
    def printInfo(self):
        print(self.__on,self.__speed,self.__color,self.__radius)


F1 = Fan()
F2 = Fan()

F1.setSpeed(FAST)
F1.setRadius(10)
F1.setColor("yellow")
F1.setOn(True)
F1.printInfo()

F2.setSpeed(MEDIUM)
F2.setRadius(5)
F2.setColor("blue")
F2.setOn(False)
F2.printInfo()




