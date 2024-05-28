import requests
import xml.etree.ElementTree as ET
from tkinter import *

window = Tk()


class MainGui:
    url = 'http://data4library.kr/api/loanItemSrch'
    service_key = "f1e7e93ee1351c8e15709881906543fb843305921a8d66a87f30050077959fcb"
    queryParams = {'authKey': service_key, 'startDt': '2022-01-01', 'endDt': '2024-05-01'}

    def __init__(self):
        self.response = requests.get(self.url, params=self.queryParams)
        self.root = ET.fromstring(self.response.text)
        print(self.response.text)
        window.title("도서관 정보")
        frame = Frame(window)
        frame.pack()

        header = ["Name", "Addr", "Tel", "Url"]

        for i, col_name in enumerate(header):
            label = Label(frame, text=col_name, font=("Helvetica", 14, "bold"))
            label.grid(row=0, column=i)

        row_count = 1
        for item in self.root.iter("row"):
            SIGUN_NM = item.findtext("SIGUN_NM")
            LOCPLC_ADDR = item.findtext("LOCPLC_ADDR")
            TELNO = item.findtext("TELNO")
            HMPG_ADDR = item.findtext("HMPG_ADDR")

            data = [SIGUN_NM, LOCPLC_ADDR, TELNO, HMPG_ADDR]
            for i, value in enumerate(data):
                label = Label(frame, text=value, font=("Helvetica", 12))
                label.grid(row=row_count, column=i)

            row_count += 1

        window.mainloop()



MainGui()
