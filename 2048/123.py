from tkinter import *
from tkinter import messagebox
import random


class Game2048:
    bg_color = {
        2: '#eee4da', 4: '#ede0c8', 8: '#edc850',
        16: '#edc53f', 32: '#f67c5f', 64: '#f65e3b',
        128: '#edcf72', 256: '#edcc61', 512: '#f2b179',
        1024: '#f59563', 2048: '#edc22e', }

    color = {
        2: '#776e65', 4: '#f9f6f2', 8: '#f9f6f2',
        16: '#f9f6f2', 32: '#f9f6f2', 64: '#f9f6f2',
        128: '#f9f6f2', 256: '#f9f6f2', 512: '#776e65',
        1024: '#f9f6f2', 2048: '#f9f6f2', }

    def __init__(self, size):
        self.n = size
        self.window = Tk()
        self.window.title('2048 Game')
        self.gameArea = Frame(self.window, bg='azure3')
        self.gridCell = [[0] * self.n for _ in range(self.n)]
        self.compress = False
        self.merge = False
        self.moved = False
        self.end = False
        self.won = False
        self.score = 0
        self.board = []
        for r in range(self.n):
            rows = []
            for c in range(self.n):
                l = Label(self.gameArea, text='', bg='azure4', font=('arial', 22, 'bold'), width=4, height=2)
                l.grid(row=r, column=c, padx=7, pady=7)
                rows.append(l)
                self.board.append(rows)
        self.gameArea.pack()
        self.random_cell()
        self.random_cell()
        self.paintGrid()

        self.window.mainloop()

    def random_cell(self):
        cells = []

        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0:
                    cells.append((r, c))
        curr = random.choice(cells)
        (r, c) = curr
        self.gridCell[r][c] = 2

    def paintGrid(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0:
                    self.board[r][c].configure(text=''
                                               , bg='azure4')

                else:
                    self.board[r][c].configure(text=str(self.gridCell[r][c]),
                                               bg=self.bg_color[self.gridCell[r][c]],
                                               fg=self.color[self.gridCell[r][c]])
Game2048(4)