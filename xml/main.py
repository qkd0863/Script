import urllib
import urllib.request
from io import BytesIO
import requests
import xml.etree.ElementTree as ET
import smtplib
import tkinter.messagebox as msgbox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageTk

from collections import defaultdict
from tkinter import *
from tkinter import font

# host = "smtp.gmail.com"
# port = "587"

senderAddr = "qkd7183@gmail.com"
recipientAddr = "qkd7183@naver.com"

# msg=MIMEBase("multipart","alternative")


# HtmlPart=MIMEText(htmlF)


window = Tk()
window.geometry("1200x800+200+200")


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

        window.title("도서관 정보")
        global mainframe
        global infoframe

        mainframe = Frame(window, width=1200, height=800)
        mainframe.pack()
        infoframe = Frame(window, width=1200, height=800)
        infoframe.pack()

        # header = ["Name", "Addr", "Tel", "Url"]

        # for i, col_name in enumerate(header):
        #    label = Label(frame, text=col_name, font=("Helvetica", 14, "bold"))
        #    label.grid(row=0, column=i)




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
                "REFINE_WGS84_LOGT": REFINE_WGS84_LOGT
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

        global SearchListBox
        ListboxScrollbar = Scrollbar(SearchFrame)
        ListboxScrollbar.pack(side='right', fill='y')

        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        SearchListBox = Listbox(SearchFrame, font=TempFont, activestyle='none', width=10, height=5, borderwidth=12,
                                relief='ridge', yscrollcommand=ListboxScrollbar.set)

        num = 0

        sortList = sorted(self.List)
        for i in sortList:
            SearchListBox.insert(num, i)
            num += 1

        SearchListBox.pack()
        ListboxScrollbar.config(command=SearchListBox.yview)

    def InitSearchButton(self):
        TempFont = font.Font(mainframe, size=12, weight='bold', family='Consolas')
        SearchButton = Button(mainframe, font=TempFont, text="검색", command=self.SearchButtonAction)
        SearchButton.place(x=50, y=50)

    def SearchButtonAction(self):
        selected_indices = SearchListBox.curselection()
        selected_index = selected_indices[0]
        SIGUN_NM = SearchListBox.get(selected_index)

        num = 0
        LibraryNameBox.delete(0, END)
        List = []

        for dictlist in self.SigunData[SIGUN_NM]:
            List.append(dictlist["LIBRRY_NM"])
        List.sort()
        for i in List:
            LibraryNameBox.insert(num, i)
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
        selected_indices = LibraryNameBox.curselection()
        if not selected_indices:
            return
        selected_index = selected_indices[0]
        LIBRRY_NM = LibraryNameBox.get(selected_index)

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

        global LibraryNameBox
        ListboxScrollbar = Scrollbar(LibraryNameFrame)
        ListboxScrollbar.pack(side='right', fill='y')

        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        LibraryNameBox = Listbox(LibraryNameFrame, font=TempFont, activestyle='none', width=20, height=5,
                                 borderwidth=12,
                                 relief='ridge', yscrollcommand=ListboxScrollbar.set)

        LibraryNameBox.pack()
        ListboxScrollbar.config(command=LibraryNameBox.yview)

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
