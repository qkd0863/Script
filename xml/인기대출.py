import requests
import xml.etree.ElementTree as ET
import tkinter

# 병원정보 서비스 예제


url = 'http://data4library.kr/api/loanItemSrch'

service_key = "f1e7e93ee1351c8e15709881906543fb843305921a8d66a87f30050077959fcb"

queryParams = {'authKey': service_key, 'startDt': '2022-01-01', 'endDt': '2024-05-01'}

response = requests.get(url, params=queryParams)
print(response.text)
root = ET.fromstring(response.text)

window = tkinter.Tk()
window.title("도서관 정보")

frame = tkinter.Frame(window)
frame.pack()

header = ["Name", "Addr", "Tel", "Url"]

for i, col_name in enumerate(header):
    label = tkinter.Label(frame, text=col_name, font=("Helvetica", 14, "bold"))
    label.grid(row=0, column=i)

row_count = 1
for item in root.iter("row"):
    SIGUN_NM = item.findtext("SIGUN_NM")
    LOCPLC_ADDR = item.findtext("LOCPLC_ADDR")
    TELNO = item.findtext("TELNO")
    HMPG_ADDR = item.findtext("HMPG_ADDR")

    data = [SIGUN_NM, LOCPLC_ADDR, TELNO, HMPG_ADDR]
    for i, value in enumerate(data):
        label = tkinter.Label(frame, text=value, font=("Helvetica", 12))
        label.grid(row=row_count, column=i)

    row_count += 1

window.mainloop()
