from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename


def openFile():
    fn = askopenfilename()
    filename.set(fn)


def showResult2():
    fn = filename.get()
    try:
        infile = open(fn, "r")
        counts = [0] * 26
        for line in infile:
            lowerLine = line.lower()
            for ch in lowerLine:
                if ch.isalpha():
                    counts[ord(ch) - ord('a')] += 1

        width = int(canvas['width'])
        height = int(canvas['height'])
        maxCounts = max(counts)
        heightBar = height * 0.75
        widthBar = width - 20

        for i in range(26):
            canvas.create_rectangle(i * widthBar / 26 + 10, height - heightBar * counts[i] / maxCounts - 20,
                                    (i + 1) * widthBar / 26,
                                    height - 20)
            canvas.create_text(i * width / 26 + 10 + 0.5 * widthBar / 26, height - 10, text=chr(i + ord('a')))
            infile.close()

    except IOError:
        tkinter.messagebox.showwarning(filename + "파일이 존재하지 않습니다.")


window = Tk()
window.title("문자의 출현 빈도수")
frame1 = Frame(window)
frame1.pack()
canvas = Canvas(frame1, width=500, height=200)
canvas.pack()

frame2 = Frame(window)
frame2.pack()
Label(frame2, text="파일명을 입력하세요:").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text="열기", command=openFile).pack(side=LEFT)
Button(frame2, text="결과보기", command=showResult2).pack(side=LEFT)
window.mainloop()
