from tkinter import *
import tkinter.ttk
window=Tk()
window.title("노트북")
notebook=tkinter.ttk.Notebook(window,width=800,height=600)
notebook.pack()
frame1=Frame(window)
notebook.add(frame1,text='페이지1')
Label(frame1,text='페이지1의 내용',bg='red',font='helvetica 48').pack()
frame2=Frame(window)
notebook.add(frame2,text='페이지2')
Label(frame2,text='페이지2의 내용',bg='red',font='helvetica 48').pack()
frame3=Frame(window)
notebook.add(frame3,text='페이지3')
Label(frame3,text='페이지3의 내용',bg='red',font='helvetica 48').pack()

window.mainloop()