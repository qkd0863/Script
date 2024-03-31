from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename


def openFile():
    fn = askopenfilename()
    filename.set(fn)


def showResult():
    fn = filename.get()
    try:
        infile = open(fn, "r")
        counts = [0] * 26
        for line in infile:
            lowerLine = line.lower()
            for ch in lowerLine:
                if ch.isalpha():
                    counts[ord(ch) - ord('a')] += 1
        for i in range(26):
            if counts[i] != 0:
                text.insert(END, chr(i + ord('a')) + " - " + str(counts[i]) + "번 나타납니다.\n")
        infile.close()

    except IOError:
        tkinter.messagebox.showwarning(filename + "파일이 존재하지 않습니다.")


window = Tk()
window.title("문자의 출현 빈도수")
frame1 = Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)
frame2 = Frame(window)
frame2.pack()
Label(frame2, text="파일명을 입력하세요:").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text="열기", command=openFile).pack(side=LEFT)
Button(frame2, text="결과보기", command=showResult).pack(side=LEFT)
window.mainloop()
