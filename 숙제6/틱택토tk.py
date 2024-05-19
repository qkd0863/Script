from tkinter import *


class MainGui:
    def check(self):
        for i in range(3):
            player = self.matrix[i][0]['text']
            if player != ' ' and player == self.matrix[i][1]['text'] and player == self.matrix[i][2]['text']:
                return player

            player = self.matrix[0][i]['text']
            if player != ' ' and player == self.matrix[1][i]['text'] and player == self.matrix[2][i]['text']:
                return player

        player = self.matrix[0][0]['text']
        if player != ' ' and player == self.matrix[1][1]['text'] and player == self.matrix[2][2]['text']:
            return player
        player = self.matrix[0][2]['text']
        if player != ' ' and player == self.matrix[1][1]['text'] and player == self.matrix[2][0]['text']:
            return player
        return ' '

    def pressed(self, row, col):
        if not self.done and self.matrix[row][col]['text'] == ' ':
            if self.turn:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] = 'X'
            else:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'O'
            self.turn = not self.turn
            if self.check() != ' ':
                self.done = True
                self.explain.set('플레이어'+ self.check()+ '이겼습니다')
            elif self.turn:
                self.explain.set('플레이어 X차례')
            else:
                self.explain.set('플레이어 O차례')

    def refresh(self):
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
        self.done = False
        self.explain.set('플레이어 X차례')
        self.turn = True

    def __init__(self):
        window = Tk()
        window.title("틱택토")
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageX = PhotoImage(file='image/cross.gif')
        self.imageO = PhotoImage(file='image/circle.gif')
        self.imageE = PhotoImage(file='image/empty.gif')
        self.turn = True
        self.done = False
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                self.matrix[i].append(
                    Button(frame, image=self.imageE, text=' ', command=lambda row=i, col=j: self.pressed(row, col)))
                self.matrix[i][j].grid(row=i, column=j)

        frame1 = Frame(window)
        frame1.pack()
        self.explain = StringVar()
        self.explain.set('플레이어 X차례')
        self.label = Label(frame1, textvariable=self.explain)
        self.label.pack(side=LEFT)
        Button(frame1, text='다시 실행', command=self.refresh).pack()

        window.mainloop()


MainGui()
