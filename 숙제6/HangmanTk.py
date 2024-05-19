import random
from tkinter import *


class MainGUI:
    def toString(self, guessWord):
        result = ''
        for ch in guessWord:
            result += ch
        return result

    def drawHangman(self):
        self.canvas.delete('hangman')
        self.canvas.create_arc(20, 200, 20 + 80, 200 + 40, start=0, extent=180)
        self.canvas.create_line(20 + 40, 200, 20 + 40, 20)
        self.canvas.create_line(20 + 40, 20, 20 + 40 + 100, 20)

        if self.doneWithWrong:
            self.canvas.create_text(200, 250, text='정답' + self.toString(self.hiddenword), font='Time 14',
                                    tags='hangman')

            self.canvas.create_text(200, 270, text='계속하려면 enter', font='Time 14',
                                    tags='hangman')

        elif self.doneWithCorret:
            self.canvas.create_text(200, 250, text='맞았습니다' + self.toString(self.hiddenword), font='Time 14',
                                    tags='hangman')

            self.canvas.create_text(200, 270, text='계속하려면 enter', font='Time 14',
                                    tags='hangman')
        else:
            self.canvas.create_text(200, 250, text='단어 추측' + self.toString(self.guessword), font='Time 14',
                                    tags='hangman')
            if self.NofMiss > 0:
                self.canvas.create_text(200, 270, text='틀린 글자' + self.toString(self.missChars), font='Time 14',
                                        tags='hangman')
        if self.NofMiss < 1:
            return
        x1 = 20 + 40 + 100
        y1 = 20
        x2 = x1
        y2 = y1 + 20
        self.canvas.create_line(x1, y1, x2, y2, tags='hangman')
        if self.NofMiss < 2:
            return
        x3 = x2
        y3 = y2 + 40
        self.canvas.create_oval(x3 - 20, y3 - 20, x3 + 20, y3 + 20, tags='hangman')

        if self.NofMiss < 3:
            return
        self.canvas.create_line(x3 - 15, y3 + 15, x3 - 50, y3 + 70, tags='hangman')
        if self.NofMiss < 4:
            return
        self.canvas.create_line(x3 + 15, y3 + 15, x3 + 50, y3 + 70, tags='hangman')

        if self.NofMiss < 5:
            return
        x4 = x3
        y4 = y3 + 100
        self.canvas.create_line(x3, y3 + 20, x4, y4, tags='hangman')

        if self.NofMiss < 6:
            return
        x4 = x3
        y4 = y3 + 100
        self.canvas.create_line(x4, y4, x4 - 50, y4 + 100, tags='hangman')

        if self.NofMiss < 7:
            return
        self.canvas.create_line(x4, y4, x4 + 50, y4 + 100, tags='hangman')

    def setWord(self):
        index = random.randint(0, len(self.words) - 1)
        self.hiddenword = self.words[index]
        self.guessword = ['*'] * len(self.hiddenword)
        self.NofCorretChar = 0
        self.NofMiss = 0
        self.missChars = []
        self.doneWithWrong = False
        self.doneWithCorret = False

    def KeyEvent(self, Key):
        if 'a' <= Key.char <= 'z':
            if Key.char in self.guessword:
                print('\tt', Key.char, '은 이미 포함되어 있습니다')
            elif self.hiddenword.find(Key.char) < 0:
                print(('\t', Key.char, '은 포함되어 있지 않습니다'))
                self.NofMiss += 1
                if not Key.char in self.missChars:
                    self.missChars.append(Key.char)
                if self.NofMiss == 7:
                    self.doneWithWrong = True
            else:
                k = self.hiddenword.find(Key.char)
                while k >= 0:
                    self.guessword[k] = Key.char
                    self.NofCorretChar += 1
                    k = self.hiddenword.find(Key.char, k + 1)
                if self.NofCorretChar == len(self.hiddenword):
                    self.doneWithCorret = True
        elif Key.keycode == 13:
            if self.doneWithCorret or self.doneWithWrong:
                self.setWord()
                self.drawHangman()
        self.drawHangman()

    def __init__(self):
        fp = open('hangman.txt')
        self.words = fp.read().split()
        window = Tk()
        window.title('행맨 게임')
        self.canvas = Canvas(window, bg='white', width=400, height=300)
        self.canvas.pack()
        self.setWord()
        self.drawHangman()

        self.canvas.bind('<Key>', self.KeyEvent)
        self.canvas.focus_set()
        window.mainloop()


MainGUI()
