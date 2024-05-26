import requests
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import font

# 병원정보 서비스 예제

window = Tk()
window.geometry("1200x800+200+200")


class MainGui():
    url = 'https://openapi.gg.go.kr/TBGGIBLLBR'
    service_key = "94c80014751c43c3aff04a8290cda503"
    queryParams = {'KEY': service_key, 'Type': 'xml', 'pIndex': '1', 'pSize': '100'}
    response = requests.get(url, params=queryParams)
    root = ET.fromstring(response.text)
    List = set()

    def __init__(self):

        window.title("도서관 정보")

        frame = Frame(width=100,height=80)
        frame.place(x=200,y=200)

        header = ["Name", "Addr", "Tel", "Url"]

        for i, col_name in enumerate(header):
            label = Label(frame, text=col_name, font=("Helvetica", 14, "bold"))
            label.grid(row=0, column=i)

        row_count = 1
        for item in self.root.iter("row"):
            SIGUN_NM = item.findtext("SIGUN_NM")
            self.List.add(item.findtext("SIGUN_NM"))
            LOCPLC_ADDR = item.findtext("LOCPLC_ADDR")
            TELNO = item.findtext("TELNO")
            HMPG_ADDR = item.findtext("HMPG_ADDR")

            #data = [SIGUN_NM, LOCPLC_ADDR, TELNO, HMPG_ADDR]
            #for i, value in enumerate(data):
            #    label = Label(frame, text=value, font=("Helvetica", 12))
            #    label.grid(row=row_count, column=i)

            row_count += 1

        self.InitTopText()
        self.InitSearchListBox()

        window.mainloop()

    def InitTopText(self):
        self.TopText = Label(window, text="경기도 도서관 정보 검색")
        self.TopText.pack()
        self.TopText.place(x=20, y=0)

    def InitSearchListBox(self):
        SearchFrame=Frame(width=100,height=100)
        SearchFrame.place(x=10,y=10)

        global SearchListBox
        ListboxScrollbar = Scrollbar(SearchFrame)
        ListboxScrollbar.pack(side='right',fill='y')
        ListboxScrollbar.place(x=150, y=200)

        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        SearchListBox = Listbox(SearchFrame, font=TempFont, activestyle='none', width=10, height=5, borderwidth=12,
                                relief='ridge', yscrollcommand=ListboxScrollbar.set)

        num = 0
        for i in self.List:
            SearchListBox.insert(num + 1, i)
            num += 1


        SearchListBox.place(x=10, y=200)
        ListboxScrollbar.config(command=SearchListBox.yview)


MainGui()
