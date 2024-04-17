from tkinter import *
from random import *

width = 800
height = 600


class Ball:
    def toHexChar(self, value):
        if 0 <= value <= 9:
            return chr(value + ord('0'))
        else:
            return chr(value - 10 + ord('A'))

    def getRandomColor(self):
        color = '#'
        for i in range(6):
            color += self.toHexChar(randint(0, 15))
        return color

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.color = self.getRandomColor()


class MainGUI:
    def stop(self):
        self.isStoped = True

    def resume(self):
        self.isStoped = False
        self.animate()

    def add(self):
        self.ballList.append(Ball())

    def remove(self):
        self.ballList.pop()

    def faster(self):
        if self.sleepTime>20:
            self.sleepTime-=20

    def slower(self):
        self.sleepTime += 20


    def displayBall(self, ball):
        if ball.x >= width:
            ball.dx = -2
        elif ball.x < 0:
            ball.dx = 2

        if ball.y >= height:
            ball.dy = -2
        elif ball.y < 0:
            ball.dy = 2

        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - 3, ball.y - 3, ball.x + 3, ball.y + 3, fill=ball.color, tags='ball')

    def animate(self):
        while not self.isStoped:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete('ball')
            for ball in self.ballList:
                self.displayBall(ball)

    def __init__(self):
        window = Tk()
        window.title("공 튕기기")
        self.ballList = []
        self.isStoped = False
        self.sleepTime = 100
        self.canvas = Canvas(window, bg='white', width=width, height=height)
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Button(frame, text="정지", command=self.stop).pack(side=LEFT)
        Button(frame, text="재시작", command=self.resume).pack(side=LEFT)
        Button(frame, text="+", command=self.add).pack(side=LEFT)
        Button(frame, text="-", command=self.remove).pack(side=LEFT)
        Button(frame, text="빠르게", command=self.faster).pack(side=LEFT)
        Button(frame, text="느리게", command=self.slower).pack(side=LEFT)
        self.animate()
        window.mainloop()


MainGUI()
