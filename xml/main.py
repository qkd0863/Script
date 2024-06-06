import certifi
import urllib.request
from io import BytesIO
import requests
import xml.etree.ElementTree as ET
import smtplib
import tkinter.messagebox as msgbox
import telepot
import spam
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageTk

from collections import defaultdict
from tkinter import *
from tkinter import font
from googlemaps import Client

senderAddr = "qkd7183@gmail.com"

google_key = "AIzaSyBAAAqcV4L-qDCewx1tmO91hfb77NWen1I"
gmaps = Client(key=google_key)

window = Tk()
window.geometry("1200x800+200+200")

width = 800
height = 600


class MainGui():
    book_url = 'http://data4library.kr/api/loanItemSrch'
    book_service_key = "f1e7e93ee1351c8e15709881906543fb843305921a8d66a87f30050077959fcb"
    book_queryParams = {'authKey': book_service_key, 'startDt': '2024-01-01', 'endDt': '2024-05-01'}
    book_response = requests.get(book_url, params=book_queryParams)
    book_root = ET.fromstring(book_response.text)
    url = 'https://openapi.gg.go.kr/TBGGIBLLBR'
    service_key = "94c80014751c43c3aff04a8290cda503"
    queryParams = {'KEY': service_key, 'Type': 'xml', 'pIndex': '1', 'pSize': '1000'}
    response = requests.get(url, params=queryParams)
    root = ET.fromstring(response.text)
    List = set()
    Book_List = set()

    def __init__(self):
        self.select_sigun = 0

        window.title("도서관 정보")
        global mainframe
        global infoframe

        mainframe = Frame(window, width=1200, height=800)
        mainframe.pack()
        infoframe = Frame(window, width=1200, height=800)
        infoframe.pack()

        self.Book_List_Data = []
        for item in self.book_root.iter("doc"):
            self.Book_List.add(item.findtext("bookname"))

            temp = []
            temp.append(item.findtext("bookname"))
            temp.append(item.findtext("authors"))
            temp.append(item.findtext("publisher"))
            temp.append(item.findtext("publication_year"))
            temp.append(item.findtext("vol"))
            temp.append(item.findtext("bookImageURL"))
            self.Book_List_Data.append(temp)

        self.SigunData = defaultdict(list)
        for item in self.root.iter("row"):
            SIGUN_NM = item.findtext("SIGUN_NM")
            self.List.add(item.findtext("SIGUN_NM"))
            LOCPLC_ADDR = item.findtext("LOCPLC_ADDR")
            TELNO = item.findtext("TELNO")
            HMPG_ADDR = item.findtext("HMPG_ADDR")
            LIBRRY_NM = item.findtext("LIBRRY_NM")
            RECSROOM_OPEN_TM_INFO = item.findtext("RECSROOM_OPEN_TM_INFO")
            READROOM_OPEN_TM_INFO = item.findtext("READROOM_OPEN_TM_INFO")
            RECSROOM_REST_DE_INFO = item.findtext("RECSROOM_REST_DE_INFO")
            READROOM_REST_DE_INFO = item.findtext("READROOM_REST_DE_INFO")
            REFINE_WGS84_LAT = item.findtext("REFINE_WGS84_LAT")
            REFINE_WGS84_LOGT = item.findtext("REFINE_WGS84_LOGT")
            DMSTC_BOOK_DATA_CNT = item.findtext("DMSTC_BOOK_DATA_CNT")
            FRN_BOOK_DATA_CNT = item.findtext("FRN_BOOK_DATA_CNT")
            self.SigunData[SIGUN_NM].append({
                "LOCPLC_ADDR": LOCPLC_ADDR,
                "TELNO": TELNO,
                "HMPG_ADDR": HMPG_ADDR,
                "LIBRRY_NM": LIBRRY_NM,
                "RECSROOM_OPEN_TM_INFO": RECSROOM_OPEN_TM_INFO,
                "READROOM_OPEN_TM_INFO": READROOM_OPEN_TM_INFO,
                "RECSROOM_REST_DE_INFO": RECSROOM_REST_DE_INFO,
                "READROOM_REST_DE_INFO": READROOM_REST_DE_INFO,
                "REFINE_WGS84_LAT": REFINE_WGS84_LAT,
                "REFINE_WGS84_LOGT": REFINE_WGS84_LOGT,
                "DMSTC_BOOK_DATA_CNT": DMSTC_BOOK_DATA_CNT,
                "FRN_BOOK_DATA_CNT": FRN_BOOK_DATA_CNT
            })

        self.InitBackButton()
        self.InitTopText()
        self.InitSearchButton()
        self.InitSearchListBox()
        self.InitLibraryNameListBox()
        self.InitLibraryInformationButton()
        self.InitLenderText()
        self.InitBookListBox()
        self.InitBookInfoLenderText()
        self.InitBookInfoButton()
        self.InitSendMailButton()
        self.InitBookImageLabel()
        self.InitTeleButton()
        self.InitGraphButton()

        window.mainloop()

    def openFrame(self, frame):
        mainframe.pack_forget()
        infoframe.pack(fill="both", expand=True)
        frame.tkraise()

    def openInfoFrame(self):
        infoframe.pack_forget()
        mainframe.pack(fill="both", expand=True)

    def InitBackButton(self):
        TempFont = font.Font(infoframe, size=12, weight='bold', family='Consolas')
        SearchButton = Button(infoframe, font=TempFont, text="뒤로가기", command=self.BackButtonAction)
        SearchButton.place(x=50, y=50)

    def BackButtonAction(self):
        BookInfoLenderText.config(state=NORMAL)
        BookInfoLenderText.delete('1.0', END)
        BookInfoLenderText.configure(state='disabled')

        RenderText.config(state=NORMAL)
        RenderText.delete('1.0', END)

        if hasattr(self, 'book_image_label'):
            self.book_image_label.destroy()

        self.openInfoFrame()

    def InitTopText(self):
        self.TopText = Label(mainframe, text="경기도 공공도서관 정보 검색")
        self.TopText.place(x=20, y=0)

    def InitSearchListBox(self):
        SearchFrame = Frame(mainframe)
        SearchFrame.place(x=0, y=100)

        ListboxScrollbar = Scrollbar(SearchFrame)
        ListboxScrollbar.pack(side='right', fill='y')

        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        self.SearchListBox = Listbox(SearchFrame, font=TempFont, activestyle='none', width=10, height=5, borderwidth=12,
                                     relief='ridge', yscrollcommand=ListboxScrollbar.set)

        num = 0

        sortList = sorted(self.List)
        for i in sortList:
            self.SearchListBox.insert(num, i)
            num += 1

        self.SearchListBox.pack()
        ListboxScrollbar.config(command=self.SearchListBox.yview)

        self.SearchListBox.bind('<ButtonRelease-1>', self.OnListBoxSelect)

    def OnListBoxSelect(self, event):
        selected_indices = self.SearchListBox.curselection()
        selected_index = selected_indices[0]
        SIGUN_NM = self.SearchListBox.get(selected_index)

        self.select_sigun = SIGUN_NM
        self.UpdateMap(SIGUN_NM)

    def OnNameBoxSelect(self, event):
        selected_indices = self.LibraryNameBox.curselection()
        selected_index = selected_indices[0]
        Library_Name = self.LibraryNameBox.get(selected_index)

        self.UpdateMap_OneMark(self.select_sigun, Library_Name)

    def UpdateMap(self, SIGUN_NM):
        gmaps_api_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": SIGUN_NM,
            "key": google_key
        }
        print(params["address"])

        response = requests.get(gmaps_api_url, params=params)
        response.raise_for_status()
        center = response.json()["results"][0]["geometry"]["location"]

        seoul_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={center['lat']},{center['lng']}&zoom=11&size=1000x1000&maptype=roadmap&key={google_key}"

        for library in self.SigunData[SIGUN_NM]:
            lat = library['REFINE_WGS84_LAT']
            lng = library['REFINE_WGS84_LOGT']
            library_name = library['LIBRRY_NM']
            marker = f"&markers=color:red%7Clabel:{library_name[0]}%7C{lat},{lng}"
            seoul_map_url += marker

        response = requests.get(seoul_map_url)
        response.raise_for_status()

        image_data = response.content
        photo = ImageTk.PhotoImage(data=image_data)

        if hasattr(self, 'map_label'):
            self.map_label.destroy()

        self.map_label = Label(mainframe, image=photo)
        self.map_label.image = photo
        self.map_label.place(x=500, y=100)

    def UpdateMap_OneMark(self, SIGUN_NM, Library_Name):
        gmaps_api_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": SIGUN_NM,
            "key": google_key
        }

        response = requests.get(gmaps_api_url, params=params)
        response.raise_for_status()
        center = response.json()["results"][0]["geometry"]["location"]

        seoul_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={center['lat']},{center['lng']}&zoom=11&size=1000x1000&maptype=roadmap&key={google_key}"

        for library in self.SigunData[SIGUN_NM]:
            if Library_Name == library['LIBRRY_NM']:
                lat = library['REFINE_WGS84_LAT']
                lng = library['REFINE_WGS84_LOGT']
                library_name = library['LIBRRY_NM']
                marker = f"&markers=color:red%7Clabel:{library_name[0]}%7C{lat},{lng}"
                seoul_map_url += marker

        response = requests.get(seoul_map_url)
        response.raise_for_status()

        image_data = response.content
        photo = ImageTk.PhotoImage(data=image_data)

        if hasattr(self, 'map_label'):
            self.map_label.destroy()

        self.map_label = Label(mainframe, image=photo)
        self.map_label.image = photo
        self.map_label.place(x=500, y=100)

    def InitTeleButton(self):
        TempFont = font.Font(mainframe, size=12, weight='bold', family='Consolas')
        TeleButton = Button(mainframe, font=TempFont, text="텔레그램 봇", command=self.TeleButtonAction)
        TeleButton.place(x=50, y=700)

    def TeleButtonAction(self):
        pass

    def InitGraphButton(self):
        TempFont = font.Font(mainframe, size=12, weight='bold', family='Consolas')
        GraphButton = Button(mainframe, font=TempFont, text="그래프 출력", command=self.GraphButtonAction)
        GraphButton.place(x=200, y=700)

    def GraphButtonAction(self):
        self.WriteGraphWindow()

    def WriteGraphWindow(self):
        global GraphWindow
        GraphWindow = Toplevel()
        GraphWindow.geometry("1200x800+200+200")
        GraphWindow.title("국내도서 자료수")

        # Create a frame to hold the canvas and scrollbar
        frame = Frame(GraphWindow)
        frame.pack(fill=BOTH, expand=True)

        # Create the canvas
        self.canvas = Canvas(frame, width=1200, height=400, bg='white')
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Create the scrollbar
        self.scrollbar_x = Scrollbar(frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.scrollbar_x.grid(row=1, column=0, sticky="ew")

        # Configure the canvas to work with the scrollbar
        self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        Domestic_button = Button(GraphWindow, text="국내도서", font=("Helvetica", 12), command=self.Domestic_button_Action)
        Domestic_button.pack(pady=30)

        Oversea_button = Button(GraphWindow, text="국외도서", font=("Helvetica", 12), command=self.Domestic_button_Action)
        Oversea_button.pack(pady=30)

        SearchFrame = Frame(GraphWindow)
        SearchFrame.place(x=0, y=615)

        ListboxScrollbar = Scrollbar(SearchFrame)
        ListboxScrollbar.pack(side='right', fill='y')

        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        self.GraphListBox = Listbox(SearchFrame, font=TempFont, activestyle='none', width=10, height=5, borderwidth=12,
                                    relief='ridge', yscrollcommand=ListboxScrollbar.set)

        num = 0

        sortList = sorted(self.List)
        for i in sortList:
            self.GraphListBox.insert(num, i)
            num += 1

        self.GraphListBox.pack()
        ListboxScrollbar.config(command=self.GraphListBox.yview)

        self.GraphListBox.bind('<ButtonRelease-1>', self.OnGraphBoxSelect)
        self.BookNumList = []

    def OnGraphBoxSelect(self, event):
        selected_indices = self.GraphListBox.curselection()
        selected_index = selected_indices[0]
        SIGUN_NM = self.GraphListBox.get(selected_index)

        self.BookNumList = []

        for data in self.SigunData[SIGUN_NM]:
            dmstc_book_count = int(data["DMSTC_BOOK_DATA_CNT"]) if data["DMSTC_BOOK_DATA_CNT"].strip() else 0
            frn_book_count = int(data["FRN_BOOK_DATA_CNT"]) if data["FRN_BOOK_DATA_CNT"].strip() else 0
            self.BookNumList.append((data["LIBRRY_NM"], dmstc_book_count, frn_book_count))

    def Domestic_button_Action(self):
        barWidth = 50
        barGap = 100

        sorted_domestic = sorted(self.BookNumList, key=lambda x: x[1])
        sorted_oversea = sorted(self.BookNumList, key=lambda x: x[2])

        print(sorted_domestic)

        max_bar_height = 500

        self.canvas.delete("histogram")
        self.draw_bars(sorted_domestic, barWidth, barGap, max_bar_height, 'blue', 'book_count', start_x=50)

        self.draw_bars(sorted_oversea, barWidth, barGap, max_bar_height, 'red', 'book_count2',
                       start_x=50 + (barWidth + barGap) * len(sorted_domestic) + barGap)

    def draw_bars(self, sorted_data, barWidth, barGap, max_bar_height, color, text_tag, start_x):

        num_bars = len(sorted_data)
        if num_bars > 0:
            bar_height = max_bar_height / num_bars

            for i, (library_name, book_count, book_count2) in enumerate(sorted_data):

                rank = i + 1
                x1 = start_x + (barWidth + barGap) * i
                y1 = 600 - rank * bar_height
                x2 = x1 + barWidth
                y2 = 600

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags='histogram')

                if text_tag == 'book_count':
                    text_value = str(book_count)
                elif text_tag == 'book_count2':
                    text_value = str(book_count2)

                self.canvas.create_text((x1 + x2) / 2, y1 - 10, text=text_value, anchor='s', tags='histogram')
                self.canvas.create_text((x1 + x2) / 2, y2 + 10, text=library_name, anchor='n', tags='histogram')

        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

    def InitSearchButton(self):
        TempFont = font.Font(mainframe, size=12, weight='bold', family='Consolas')
        SearchButton = Button(mainframe, font=TempFont, text="검색", command=self.SearchButtonAction)
        SearchButton.place(x=50, y=50)

    def SearchButtonAction(self):
        selected_indices = self.SearchListBox.curselection()
        selected_index = selected_indices[0]
        SIGUN_NM = self.SearchListBox.get(selected_index)

        num = 0
        self.LibraryNameBox.delete(0, END)
        List = []

        for dictlist in self.SigunData[SIGUN_NM]:
            List.append(dictlist["LIBRRY_NM"])
        List.sort()
        for i in List:
            self.LibraryNameBox.insert(num, i)
            num += 1

    def InitLibraryInformationButton(self):
        TempFont = font.Font(mainframe, size=12, weight='bold', family='Consolas')
        SearchButton = Button(mainframe, font=TempFont, text="도서관 정보 출력", command=self.LibraryInformationSearch)
        SearchButton.place(x=210, y=50)

    def InitLenderText(self):
        global RenderText
        RenderText = Text(infoframe, width=150, height=10, borderwidth=12, relief='ridge')
        RenderText.place(x=50, y=100)

    def LibraryInformationSearch(self):
        selected_indices = self.LibraryNameBox.curselection()
        if not selected_indices:
            return
        selected_index = selected_indices[0]
        LIBRRY_NM = self.LibraryNameBox.get(selected_index)

        for sigun, libraries in self.SigunData.items():
            for library in libraries:
                if library["LIBRRY_NM"] == LIBRRY_NM:
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, library['LIBRRY_NM'])
                    RenderText.insert(INSERT, "] 주소:")
                    RenderText.insert(INSERT, library['LOCPLC_ADDR'])
                    RenderText.insert(INSERT, "\n홈페이지 주소:")
                    RenderText.insert(INSERT, library['HMPG_ADDR'])
                    RenderText.insert(INSERT, "    전화번호:")
                    RenderText.insert(INSERT, library['TELNO'])
                    RenderText.insert(INSERT, "\n자료실 개방시간:")
                    RenderText.insert(INSERT, library['RECSROOM_OPEN_TM_INFO'])
                    RenderText.insert(INSERT, "\n열람실 개방시간:")
                    RenderText.insert(INSERT, library['READROOM_OPEN_TM_INFO'])
                    RenderText.insert(INSERT, "\n자료실 휴무일자:")
                    RenderText.insert(INSERT, library['RECSROOM_REST_DE_INFO'])
                    RenderText.insert(INSERT, "\n열람실 휴무일자:")
                    RenderText.insert(INSERT, library['READROOM_REST_DE_INFO'])
                    RenderText.insert(INSERT, "\n위도:")
                    RenderText.insert(INSERT, library['REFINE_WGS84_LAT'])
                    RenderText.insert(INSERT, "     경도:")
                    RenderText.insert(INSERT, library['REFINE_WGS84_LOGT'])

        RenderText.configure(state='disabled')
        self.openFrame(infoframe)

    def InitLibraryNameListBox(self):
        LibraryNameFrame = Frame(mainframe)
        LibraryNameFrame.place(x=160, y=100)

        ListboxScrollbar = Scrollbar(LibraryNameFrame)
        ListboxScrollbar.pack(side='right', fill='y')

        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        self.LibraryNameBox = Listbox(LibraryNameFrame, font=TempFont, activestyle='none', width=20, height=5,
                                      borderwidth=12,
                                      relief='ridge', yscrollcommand=ListboxScrollbar.set)

        self.LibraryNameBox.pack()
        ListboxScrollbar.config(command=self.LibraryNameBox.yview)

        self.LibraryNameBox.bind('<ButtonRelease-1>', self.OnNameBoxSelect)

    def InitBookListBox(self):
        BookListFrame = Frame(infoframe)
        BookListFrame.place(x=50, y=280)

        global BookListBox
        BookListboxScrollbar = Scrollbar(BookListFrame)
        BookListboxScrollbar.pack(side='right', fill='y')

        TempFont = font.Font(BookListFrame, size=15, weight='bold', family='Consolas')
        BookListBox = Listbox(BookListFrame, font=TempFont, activestyle='none', width=95, height=5, borderwidth=12,
                              relief='ridge', yscrollcommand=BookListboxScrollbar.set)

        num = 0

        sortList = sorted(self.Book_List)
        for i in sortList:
            BookListBox.insert(num, i)
        num += 1

        BookListBox.pack()
        BookListboxScrollbar.config(command=BookListBox.yview)

    def InitBookInfoButton(self):
        TempFont = font.Font(infoframe, size=12, weight='bold', family='Consolas')
        BookInfoButton = Button(infoframe, font=TempFont, text="책 정보 출력", command=self.BookInfoButtonAction)
        BookInfoButton.place(x=150, y=50)

    def BookInfoButtonAction(self):
        selected_indices = BookListBox.curselection()
        selected_index = selected_indices[0]
        bookname = BookListBox.get(selected_index)

        BookInfoLenderText.config(state=NORMAL)
        BookInfoLenderText.delete('1.0', END)
        for i in self.Book_List_Data:
            if str(i[0]) == bookname:
                BookInfoLenderText.insert(INSERT, bookname + "  ")
                BookInfoLenderText.insert(INSERT, i[1])
                BookInfoLenderText.insert(INSERT, "\n")
                BookInfoLenderText.insert(INSERT, i[2] + "  ")
                BookInfoLenderText.insert(INSERT, i[3] + "  ")
                BookInfoLenderText.insert(INSERT, i[4])
                if (i[4] != ""):
                    BookInfoLenderText.insert(INSERT, "권\n")

                url = i[5]

                if hasattr(self, 'book_image_label'):
                    self.book_image_label.destroy()

                response = requests.get(url)
                image_data = response.content
                im = ImageTk.PhotoImage(data=image_data)

                self.book_image_label = Label(infoframe, image=im)
                self.book_image_label.image = im  # keep a reference
                self.book_image_label.place(x=800, y=470)

        RenderText.configure(state='disabled')

    def InitBookInfoLenderText(self):
        global BookInfoLenderText

        BookInfoLenderText = Text(infoframe, width=80, height=20, borderwidth=12, relief='ridge')
        BookInfoLenderText.place(x=50, y=470)

    def InitBookImageLabel(self):
        pass

    def InitSendMailButton(self):
        TempFont = font.Font(infoframe, size=12, weight='bold', family='Consolas')
        SendMailButton = Button(infoframe, font=TempFont, text="도서 정보 메일 발송", command=self.WriteSendMailWindow)
        SendMailButton.place(x=300, y=50)

    def sendmail(self):
        receiver_addr = self.receiver_entry.get()
        html_content = """
        <html>
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
        <h2>인기 대출 도서 목록</h2>
        <table border="1">
        <tr>
            <th>도서명</th>
            <th>저자</th>
            <th>출판사</th>
            <th>출판 연도</th>
            <th>권수</th>
        </tr>
        """

        for book in self.Book_List_Data:
            html_content += f"""
            <tr>
                <td>{book[0]}</td>
                <td>{book[1]}</td>
                <td>{book[2]}</td>
                <td>{book[3]}</td>
                <td>{book[4]}</td>
            </tr>
            """
        html_content += """
        </table>
        </body>
        </html>
        """

        sm = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        msg = MIMEMultipart()
        msg.attach(MIMEText(html_content, 'html'))
        msg["Subject"] = "인기 대출 도서 목록"
        msg["From"] = senderAddr
        msg["To"] = receiver_addr

        new.destroy()
        try:
            sm.ehlo()
            sm.login("qkd7183@gmail.com", "cgoa ygov ukbu pijb")
            sm.sendmail(senderAddr, receiver_addr, msg.as_string())
            sm.close()
            msgbox.showinfo("성공", "메일이 정상적으로 발송되었습니다")
        except smtplib.SMTPAuthenticationError as e:
            msgbox.showwarning("실패", "로그인 실패")
        except smtplib.SMTPRecipientsRefused as e:
            msgbox.showwarning("실패", "수신 거부")
        except smtplib.SMTPException as e:
            msgbox.showwarning("실패", "이메일 전송 실패")
        except Exception as e:
            msgbox.showwarning("실패", "알 수 없는 오류가 발생")

    def WriteSendMailWindow(self):
        global new
        new = Toplevel()
        new.geometry("400x200+200+200")
        new.title("이메일 전송")

        Label(new, text="수신자 이메일 주소:", font=("Helvetica", 12)).pack(pady=10)

        self.receiver_entry = Entry(new, font=("Helvetica", 12), width=30)
        self.receiver_entry.pack()

        send_button = Button(new, text="전송", font=("Helvetica", 12), command=self.sendmail)
        send_button.pack(pady=10)

    def LoadBookListData(self):

        for item in self.book_root.iter("doc"):
            self.Book_List.add(item.findtext("bookname"))

            temp = []
            temp.append(item.findtext("bookname"))
            temp.append(item.findtext("authors"))
            temp.append(item.findtext("publisher"))
            temp.append(item.findtext("publication_year"))
            temp.append(item.findtext("vol"))
            temp.append(item.findtext("bookImageURL"))
            self.Book_List_Data.append(temp)


MainGui()
