class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self):
        v = 0
        for card in self.cards:
            if card.getVaule() == 1:
                v += 11
            else:
                v += card.getVaule()

        if v > 21:
            v = 0
            for card in self.cards:
                v += card.getVaule()
        return v
