from tkinter import *
from tkinter import font
from winsound import *
from card import *
from player import *
import random


class BlackJack:
    def __init__(self):
        self.window = Tk()
        self.window.title = ("도리짓고 땡")
        self.window.geometry("800x600")
        self.window.configure(bg='green')
        self.fontstyle = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setUpBotton()
        self.setUpLabel()

        self.player = Player('player', 1)
        self.player2 = Player('player2', 2)
        self.player3 = Player('player3', 3)
        self.dealer = Player('dealer', 1)
        self.betMoney = 0
        self.playerMoney = 1000
        self.nCardDealer = 0
        self.nCardPlayer = 0
        self.LCardPlayer = []
        self.LCardPlayer2 = []
        self.LCardPlayer3 = []
        self.LCardDealer = []
        self.deckN = 0
        self.turn = 0
        self.window.mainloop()

    def setUpBotton(self):
        self.Bet5_P1 = Button(self.window, text='5만', width=4, height=1, font=self.fontstyle2,
                              command=lambda: self.pressedBet5(self.player))
        self.Bet5_P1.place(x=10, y=500)
        self.Bet1_P1 = Button(self.window, text='1만', width=4, height=1, font=self.fontstyle2,
                              command=lambda: self.pressedBet1(self.player))
        self.Bet1_P1.place(x=80, y=500)

        self.Bet5_P2 = Button(self.window, text='5만', width=4, height=1, font=self.fontstyle2,
                              command=lambda: self.pressedBet5(self.player2))
        self.Bet5_P2.place(x=180, y=500)
        self.Bet1_P2 = Button(self.window, text='1만', width=4, height=1, font=self.fontstyle2,
                              command=lambda: self.pressedBet1(self.player2))
        self.Bet1_P2.place(x=250, y=500)

        self.Bet5_P3 = Button(self.window, text='5만', width=4, height=1, font=self.fontstyle2,
                              command=lambda: self.pressedBet5(self.player3))
        self.Bet5_P3.place(x=350, y=500)
        self.Bet1_P3 = Button(self.window, text='1만', width=4, height=1, font=self.fontstyle2,
                              command=lambda: self.pressedBet1(self.player3))
        self.Bet1_P3.place(x=420, y=500)

        self.Deal = Button(self.window, text='Deal', width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text='Again', width=6, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setUpLabel(self):
        self.LbetMoney_P1 = Label(text='$0', width=4, height=1, font=self.fontstyle, bg='green', fg='cyan')
        self.LbetMoney_P1.place(x=40, y=450)
        self.LbetMoney_P2 = Label(text='$0', width=4, height=1, font=self.fontstyle, bg='green', fg='cyan')
        self.LbetMoney_P2.place(x=200, y=450)
        self.LbetMoney_P3 = Label(text='$0', width=4, height=1, font=self.fontstyle, bg='green', fg='cyan')
        self.LbetMoney_P3.place(x=370, y=450)

        self.LplayerMoney = Label(text='1000만원', width=15, height=1, font=self.fontstyle, bg='green', fg='cyan')
        self.LplayerMoney.place(x=550, y=450)

        self.Lstatus = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lstatus.place(x=500, y=300)
        self.LplayerPts = Label(text='', width=10, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LplayerPts.place(x=0, y=250)
        self.Lplayer2Pts = Label(text='', width=10, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer2Pts.place(x=200, y=250)
        self.Lplayer3Pts = Label(text='', width=10, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer3Pts.place(x=400, y=250)
        self.LdealerPts = Label(text='', width=10, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LdealerPts.place(x=400, y=100)

        self.LplayerNum = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LplayerNum.place(x=0, y=300)
        self.Lplayer2Num = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer2Num.place(x=100, y=300)
        self.Lplayer3Num = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer3Num.place(x=200, y=300)
        self.LdealerNum = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LdealerNum.place(x=300, y=150)

        self.LplayerCard = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LplayerCard.place(x=-25, y=310)
        self.Lplayer2Card = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer2Card.place(x=160, y=310)
        self.Lplayer3Card = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer3Card.place(x=340, y=310)
        self.LdealerCard = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LdealerCard.place(x=10, y=170)

        self.LplayerWin = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LplayerWin.place(x=-25, y=285)
        self.Lplayer2Win = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer2Win.place(x=160, y=285)
        self.Lplayer3Win = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.Lplayer3Win.place(x=340, y=285)

    def pressedBet5(self, player):

        player.betMoney += 5
        if player.betMoney <= self.playerMoney:
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sounds/chip.wav', SND_FILENAME)

            if (player.playernum == 1):
                self.LbetMoney_P1.configure(text=str(player.betMoney) + "만")
                self.LplayerMoney.configure(text=str(self.playerMoney - self.sumbetMoney()) + "만원")
                return
            if (player.playernum == 2):
                self.LbetMoney_P2.configure(text=str(player.betMoney) + "만")
                self.LplayerMoney.configure(text=str(self.playerMoney - self.sumbetMoney()) + "만원")
                return
            if (player.playernum == 3):
                self.LbetMoney_P3.configure(text=str(player.betMoney) + "만")
                self.LplayerMoney.configure(text=str(self.playerMoney - self.sumbetMoney()) + "만원")
                return

        else:
            self.betMoney -= 5

    def pressedBet1(self, player):
        player.betMoney += 1
        if player.betMoney <= self.playerMoney:
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sounds/chip.wav', SND_FILENAME)

            if (player.playernum == 1):
                self.LbetMoney_P1.configure(text=str(player.betMoney) + "만")
                self.LplayerMoney.configure(text=str(self.playerMoney - self.sumbetMoney()) + "만원")
                return
            if (player.playernum == 2):
                self.LbetMoney_P2.configure(text=str(player.betMoney) + "만")
                self.LplayerMoney.configure(text=str(self.playerMoney - self.sumbetMoney()) + "만원")
                return
            if (player.playernum == 3):
                self.LbetMoney_P3.configure(text=str(player.betMoney) + "만")
                self.LplayerMoney.configure(text=str(self.playerMoney - self.sumbetMoney()) + "만원")
                return

        else:
            self.betMoney -= 1

    def firstdeal(self):
        self.player.reset()
        self.dealer.reset()
        self.cardDeck = [i for i in range(40)]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        self.hitPlayer(0, self.player)
        self.hitPlayer(0, self.player2)
        self.hitPlayer(0, self.player3)
        self.hitDealerDown(0)

        self.nCardPlayer = 1
        self.nCardDealer = 1
        self.activeBet()
        self.disalbedDeal()

    def seconddeal(self):
        for i in range(3):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.dealer.addCard(newCard)
            p = PhotoImage(file='GodoriCards/cardback.gif')
            self.LCardDealer.append(Label(self.window, image=p))
            self.LCardDealer[self.dealer.inHand() - 1].image = p
            self.LCardDealer[self.dealer.inHand() - 1].place(x=50 + (i + 1) * 25, y=50)

        for i in range(3):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player.addCard(newCard)
            p = PhotoImage(file='GodoriCards/' + newCard.filename())
            self.player.LCardPlayer.append(Label(self.window, image=p))
            self.player.LCardPlayer[self.player.inHand() - 1].image = p
            self.player.LCardPlayer[self.player.inHand() - 1].place(
                x=20 + (i + 1) * 25 + (self.player.playernum - 1) * 180, y=350)

        for i in range(3):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player2.addCard(newCard)
            p = PhotoImage(file='GodoriCards/' + newCard.filename())
            self.player2.LCardPlayer.append(Label(self.window, image=p))

            self.player2.LCardPlayer[self.player2.inHand() - 1].image = p
            self.player2.LCardPlayer[self.player2.inHand() - 1].place(
                x=20 + (i + 1) * 25 + (self.player2.playernum - 1) * 180, y=350)

        for i in range(3):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player3.addCard(newCard)
            p = PhotoImage(file='GodoriCards/' + newCard.filename())
            self.player3.LCardPlayer.append(Label(self.window, image=p))

            self.player3.LCardPlayer[self.player3.inHand() - 1].image = p
            self.player3.LCardPlayer[self.player3.inHand() - 1].place(
                x=20 + (i + 1) * 25 + (self.player3.playernum - 1) * 180, y=350)

        self.activeBet()
        self.disalbedDeal()

    def lastdeal(self):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.player.LCardPlayer.append(Label(self.window, image=p))
        self.player.LCardPlayer[self.player.inHand() - 1].image = p
        self.player.LCardPlayer[self.player.inHand() - 1].place(x=20 + 4 * 25 + (self.player.playernum - 1) * 180,
                                                                y=350)
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player2.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.player2.LCardPlayer.append(Label(self.window, image=p))
        self.player2.LCardPlayer[self.player2.inHand() - 1].image = p
        self.player2.LCardPlayer[self.player2.inHand() - 1].place(x=20 + 4 * 25 + (self.player2.playernum - 1) * 180,
                                                                  y=350)

        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player3.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.player3.LCardPlayer.append(Label(self.window, image=p))
        self.player3.LCardPlayer[self.player3.inHand() - 1].image = p
        self.player3.LCardPlayer[self.player3.inHand() - 1].place(x=20 + 4 * 25 + (self.player3.playernum - 1) * 180,
                                                                  y=350)

        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.LCardDealer.append(Label(self.window, image=p))
        self.LCardDealer[self.dealer.inHand() - 1].image = p
        self.LCardDealer[self.dealer.inHand() - 1].place(x=50 + 4 * 25, y=50)

        self.checkWiner()
        self.disabledBet()
        self.disalbedDeal()

    def deal(self):
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
        if self.turn == 0:
            self.firstdeal()
        if self.turn == 1:
            self.seconddeal()
        if self.turn == 2:
            self.lastdeal()
        self.turn += 1
        self.playerCardConfigure(self.player)
        self.playerCardConfigure(self.player2)
        self.playerCardConfigure(self.player3)

    def hitPlayer(self, n, player):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        player.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        player.LCardPlayer.append(Label(self.window, image=p))
        player.LCardPlayer[player.inHand() - 1].image = p
        player.LCardPlayer[player.inHand() - 1].place(x=20 + n * 75 + (player.playernum - 1) * 180, y=350)

    def hitDealer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.LCardDealer.append(Label(self.window, image=p))

        self.LCardDealer[self.dealer.inHand() - 1].image = p
        self.LCardDealer[self.dealer.inHand() - 1].place(x=250 + n * 30, y=50)
        # self.LdealerPts.configure(text=str(self.player.value()))

    def hitDealerDown(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='GodoriCards/cardback.gif')
        self.LCardDealer.append(Label(self.window, image=p))
        self.LCardDealer[self.dealer.inHand() - 1].image = p
        self.LCardDealer[self.dealer.inHand() - 1].place(x=50 + n * 75, y=50)
        # self.LdealerPts.configure(text=str(self.player.value()))

    def pressedDeal(self):
        self.deal()

    def pressedAgain(self):
        self.player.reset()
        self.player2.reset()
        self.player3.reset()
        self.dealer.reset()
        self.nCardDealer = 0
        self.nCardPlayer = 0

        for i in self.LCardPlayer:
            i.destroy()
        for i in self.LCardDealer:
            i.destroy()
        self.Lstatus.configure(text='')
        self.LCardPlayer = []
        self.LCardDealer = []
        self.deckN = 0
        self.turn = 0
        self.LplayerPts.configure(text='')
        self.Lplayer2Pts.configure(text='')
        self.Lplayer3Pts.configure(text='')
        self.LdealerPts.configure(text='')

        self.LplayerCard.configure(text="")
        self.Lplayer2Card.configure(text="")
        self.Lplayer3Card.configure(text="")
        self.LdealerCard.configure(text="")



        self.LplayerWin.configure(text="")
        self.Lplayer2Win.configure(text="")
        self.Lplayer3Win.configure(text="")

        for label in self.player.LCardPlayer:
            label.destroy()
        for label in self.player2.LCardPlayer:
            label.destroy()
        for label in self.player3.LCardPlayer:
            label.destroy()
        for label in self.dealer.LCardPlayer:
            label.destroy()

        self.player.LCardPlayer.clear()
        self.player2.LCardPlayer.clear()
        self.player3.LCardPlayer.clear()
        self.dealer.LCardPlayer.clear()

        self.activeBet()
        self.disalbedDeal()
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def checkWiner(self):
        self.playerMoney -= self.betMoney

        for i in range(4):
            p = PhotoImage(file='GodoriCards/' + self.dealer.cards[i].filename())
            self.LCardDealer[i].configure(image=p)
            self.LCardDealer[i].image = p

        if (self.judge(self.player, self.dealer)):
            self.LplayerWin.configure(text="승")
        else:
            self.LplayerWin.configure(text="패")

        if (self.judge(self.player2, self.dealer)):
            self.Lplayer2Win.configure(text="승")
        else:
            self.Lplayer2Win.configure(text="패")

        if (self.judge(self.player3, self.dealer)):
            self.Lplayer3Win.configure(text="승")
        else:
            self.Lplayer3Win.configure(text="패")

        self.dealerCardConfigure(self.dealer)
        self.playerPtsConfigure(self.player)
        self.playerPtsConfigure(self.player2)
        self.playerPtsConfigure(self.player3)
        self.dealerPtsConfigure(self.dealer)

        self.player.betMoney = 0
        self.player2.betMoney = 0
        self.player3.betMoney = 0

        self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
        self.LbetMoney_P1.configure(text=str(self.player.betMoney))
        self.LbetMoney_P2.configure(text=str(self.player2.betMoney))
        self.LbetMoney_P3.configure(text=str(self.player3.betMoney))

        self.disabledBet()
        self.disalbedDeal()
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

    def activeBet(self):
        self.Bet1_P1['state'] = 'active'
        self.Bet1_P1['bg'] = 'white'
        self.Bet5_P1['state'] = 'active'
        self.Bet5_P1['bg'] = 'white'
        self.Bet1_P2['state'] = 'active'
        self.Bet1_P2['bg'] = 'white'
        self.Bet5_P2['state'] = 'active'
        self.Bet5_P2['bg'] = 'white'
        self.Bet1_P3['state'] = 'active'
        self.Bet1_P3['bg'] = 'white'
        self.Bet5_P3['state'] = 'active'
        self.Bet5_P3['bg'] = 'white'

    def disabledBet(self):
        self.Bet5_P1['state'] = 'disabled'
        self.Bet5_P1['bg'] = 'gray'
        self.Bet1_P1['state'] = 'disabled'
        self.Bet1_P1['bg'] = 'gray'
        self.Bet5_P2['state'] = 'disabled'
        self.Bet5_P2['bg'] = 'gray'
        self.Bet1_P2['state'] = 'disabled'
        self.Bet1_P2['bg'] = 'gray'
        self.Bet5_P3['state'] = 'disabled'
        self.Bet5_P3['bg'] = 'gray'
        self.Bet1_P3['state'] = 'disabled'
        self.Bet1_P3['bg'] = 'gray'

    def activeDeal(self):
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def disalbedDeal(self):
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'

    def playerCardConfigure(self, player):
        Str = ""

        for i in range(len(player.cards)):
            Str += str(player.cards[i].getsuit()) + " "

        if player.playernum == 1:
            self.LplayerCard.configure(text=Str)
            return
        if player.playernum == 2:
            self.Lplayer2Card.configure(text=Str)
            return
        if player.playernum == 3:
            self.Lplayer3Card.configure(text=Str)
            return

    def dealerCardConfigure(self, dealer):
        Str = ""

        for i in range(len(dealer.cards)):
            Str += str(dealer.cards[i].getsuit()) + " "

        self.LdealerCard.configure(text=Str)

    def playerPtsConfigure(self, player):
        text = ""
        V = player.value()[0]
        V2 = player.value()[1][1]
        text2 = str(player.value()[1][0])
        if V == 5:
            text = "38광땡"
            text2 = ""
        if V == 4:
            text = "광땡"
        if V == 3:
            text = "땡"
            text2 = str(player.value()[1][1][1])
        if V == 2:
            text = "끗"
        if V == 1:
            text = "망통"
            text2 = ""
        if V == 0:
            text = "노메이드"
            text2 = ""
        if player.playernum == 1:
            self.LplayerPts.configure(text=text2 + text + " ")
            return
        if player.playernum == 2:
            self.Lplayer2Pts.configure(text=text2 + text + " ")
            return
        if player.playernum == 3:
            self.Lplayer3Pts.configure(text=text2 + text + " ")
            return

    def judge(self, player, dealer):
        if player.value()[0] > dealer.value()[0]:
            return True
        elif player.value()[0] == dealer.value()[0]:
            if player.value()[1][0] > dealer.value()[1][0]:
                return True
            else:
                return False
        else:
            return False

    def dealerPtsConfigure(self, dealer):
        text = ""
        V = dealer.value()[0]
        V2 = dealer.value()[1][1]
        text2 = str(dealer.value()[1][0])
        if V == 5:
            text = "38광땡"
            text2 = ""
        if V == 4:
            text = "광땡"
        if V == 3:
            text = "땡"
            text2 = str(dealer.value()[1][1][1])
        if V == 2:
            text = "끗"
        if V == 1:
            text = "망통"
            text2 = ""
        if V == 0:
            text = "노메이드"
            text2 = ""
        self.LdealerPts.configure(text=text2 + text + " ")

    def sumbetMoney(self):
        return self.player.betMoney + self.player2.betMoney + self.player3.betMoney


BlackJack()
