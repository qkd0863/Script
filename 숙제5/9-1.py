from tkinter import *


class MainGUI:
    def up(self):
        if (self.cy > 5):
            self.canvas.move('ball', 0, -5)
            self.cy -= 5

    def down(self):
        if (self.cy < 100):
            self.canvas.move('ball', 0, 5)
            self.cy += 5

    def left(self):
        if (self.cx > 5):
            self.canvas.move('ball', -5, 0)
            self.cx -= 5

    def right(self):
        if (self.cx < 200):
            self.canvas.move('ball', 5, 0)
            self.cx += 5

    def __init__(self):
        window = Tk()
        window.title("공 옮기기")
        width = 200
        height = 100
        self.cx = 15
        self.cy = 15
        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()
        self.canvas.create_oval(10, 10, 20, 20, fill='red', tags='ball')
        frame = Frame(window)
        frame.pack()
        Button(frame, text="상", command=self.up).pack(side=LEFT)
        Button(frame, text="하", command=self.down).pack(side=LEFT)
        Button(frame, text="좌", command=self.left).pack(side=LEFT)
        Button(frame, text="우", command=self.right).pack(side=LEFT)

        window.mainloop()


MainGUI()
