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
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
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
        self.LplayerPts = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LplayerPts.place(x=300, y=400)
        self.LdealerPts = Label(text='', width=15, height=1, font=self.fontstyle, bg='green', fg='white')
        self.LdealerPts.place(x=300, y=100)

    def pressedBet5(self, player):

        self.betMoney += 5
        if self.betMoney <= self.playerMoney:
            self.LbetMoney_P1.configure(text=str(self.betMoney) + "만")
            self.LplayerMoney.configure(text=str(self.playerMoney - self.betMoney) + "만원")
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 5

    def pressedBet1(self, player):
        self.betMoney += 1
        if self.betMoney <= self.playerMoney:
            self.LbetMoney_P1.configure(text=str(self.betMoney) + '만')
            self.LplayerMoney.configure(text=str(self.playerMoney - self.betMoney) + "만원")
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sounds/chip.wav', SND_FILENAME)
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

    def seconddeal(self):
        for i in range(3):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.dealer.addCard(newCard)
            p = PhotoImage(file='GodoriCards/cardback.gif')
            self.LCardDealer.append(Label(self.window, image=p))
            self.LCardDealer[self.dealer.inHand() - 1].image = p
            self.LCardDealer[self.dealer.inHand() - 1].place(x=50 + (i + 1) * 20, y=50)

        for i in range(3):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player.addCard(newCard)
            p = PhotoImage(file='GodoriCards/' + newCard.filename())
            self.player.LCardPlayer.append(Label(self.window, image=p))
            self.player.LCardPlayer[self.player.inHand() - 1].image = p
            self.player.LCardPlayer[self.player.inHand() - 1].place(
                x=20 + (i + 1) * 20 + (self.player.playernum - 1) * 180, y=350)

        for i in range(3):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player2.addCard(newCard)
            p = PhotoImage(file='GodoriCards/' + newCard.filename())
            self.player2.LCardPlayer.append(Label(self.window, image=p))

            self.player2.LCardPlayer[self.player2.inHand() - 1].image = p
            self.player2.LCardPlayer[self.player2.inHand() - 1].place(
                x=20 + (i + 1) * 20 + (self.player2.playernum - 1) * 180, y=350)

        for i in range(3):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player3.addCard(newCard)
            p = PhotoImage(file='GodoriCards/' + newCard.filename())
            self.player3.LCardPlayer.append(Label(self.window, image=p))

            self.player3.LCardPlayer[self.player3.inHand() - 1].image = p
            self.player3.LCardPlayer[self.player3.inHand() - 1].place(
                x=20 + (i + 1) * 20 + (self.player3.playernum - 1) * 180, y=350)

        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def lastdeal(self):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.player.LCardPlayer.append(Label(self.window, image=p))
        self.player.LCardPlayer[self.player.inHand() - 1].image = p
        self.player.LCardPlayer[self.player.inHand() - 1].place(x=20 + 4 * 20 + (self.player.playernum - 1) * 180,
                                                                y=350)
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player2.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.player2.LCardPlayer.append(Label(self.window, image=p))
        self.player2.LCardPlayer[self.player2.inHand() - 1].image = p
        self.player2.LCardPlayer[self.player2.inHand() - 1].place(x=20 + 4 * 20 + (self.player2.playernum - 1) * 180,
                                                                  y=350)

        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player3.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.player3.LCardPlayer.append(Label(self.window, image=p))
        self.player3.LCardPlayer[self.player3.inHand() - 1].image = p
        self.player3.LCardPlayer[self.player3.inHand() - 1].place(x=20 + 4 * 20 + (self.player3.playernum - 1) * 180,
                                                                  y=350)

        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.LCardDealer.append(Label(self.window, image=p))
        self.LCardDealer[self.dealer.inHand() - 1].image = p
        self.LCardDealer[self.dealer.inHand() - 1].place(x=50 + 4 * 20, y=50)

        self.checkWiner()

    def deal(self):
        if self.turn == 0:
            self.firstdeal()
        if self.turn == 1:
            self.seconddeal()
        if self.turn == 2:
            self.lastdeal()
        self.turn += 1

        self.Bet1_P1['state'] = 'active'
        self.Bet1_P1['bg'] = 'white'
        self.Bet5_P1['state'] = 'active'
        self.Bet5_P1['bg'] = 'white'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'

    def hitPlayer(self, n, player):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        player.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        player.LCardPlayer.append(Label(self.window, image=p))
        player.LCardPlayer[player.inHand() - 1].image = p
        player.LCardPlayer[player.inHand() - 1].place(x=20 + n * 75 + (player.playernum - 1) * 180, y=350)
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='GodoriCards/' + newCard.filename())
        self.LCardDealer.append(Label(self.window, image=p))

        self.LCardDealer[self.dealer.inHand() - 1].image = p
        self.LCardDealer[self.dealer.inHand() - 1].place(x=250 + n * 30, y=50)
        # self.LdealerPts.configure(text=str(self.player.value()))
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealerDown(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='GodoriCards/cardback.gif')
        self.LCardDealer.append(Label(self.window, image=p))
        self.LCardDealer[self.dealer.inHand() - 1].image = p
        self.LCardDealer[self.dealer.inHand() - 1].place(x=50 + n * 75, y=50)
        # self.LdealerPts.configure(text=str(self.player.value()))
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def pressedDeal(self):
        self.deal()

    def pressedAgain(self):
        self.player.reset()
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
        self.LdealerPts.configure(text='')

        self.Bet1_P1['state'] = 'active'
        self.Bet1_P1['bg'] = 'white'
        self.Bet5_P1['state'] = 'active'
        self.Bet5_P1['bg'] = 'white'

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def checkWiner(self):
        self.playerMoney -= self.betMoney

        for i in range(4):
            p = PhotoImage(file='GodoriCards/' + self.dealer.cards[i].filename())
            self.LCardDealer[i].configure(image=p)
            self.LCardDealer[i].image = p

        self.LplayerPts.configure(text=str(self.player.value()[1]))
        self.LdealerPts.configure(text=str(self.dealer.value()[1]))

        self.betMoney = 0
        self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
        self.LbetMoney_P1.configure(text='$' + str(self.betMoney))

        self.Bet5_P1['state'] = 'disabled'
        self.Bet5_P1['bg'] = 'gray'
        self.Bet1_P1['state'] = 'disabled'
        self.Bet1_P1['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'


BlackJack()
