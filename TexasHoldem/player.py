class Player:
    TOP = 0
    ONEPAIR = 1
    TWOPAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    BACKSTAIGHT = 5
    MOUNTAIN = 6
    FLUSH = 7
    FULLHOUSE = 8
    FOURCARD = 9
    STRAIGHTFLUSH = 10
    BACKSTAIGHTFLUSH = 11
    ROYALSTAIGHTFLUSH = 12

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
        if self.scoreRoyalStraightFlush():
            return [self.ROYALSTAIGHTFLUSH, self.scoreTop()]
        if self.scoreFlush():
            return [self.FLUSH, self.scoreTop()]

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

    def scoreRoyalStraightFlush(self):
        card = []
        for i in range(7):
            card.insert(i, [self.cards[i].getsuit(), self.cards[i].getVaule()])
        if 10 in card and 11 in card and 12 in card and 13 in card and 1 in card:
            if self.scoreFlush():
                return True
        else:
            return False

    def scoreBackStraightFlush(self):
        pass

    def scoreStraightFlush(self):
        if self.scoreFlush():
            if self.scoreStraight():
                return True
        return False

    def scoreFourCard(self):
        pass

    def scoreFullHouse(self):
        pass

    def scoreFlush(self):
        Clubs = 0
        Spades = 0
        Hearts = 0
        Diamonds = 0
        for i in range(7):
            if self.cards[i].getsuit() == 'Clubs':
                Clubs += 1
            if self.cards[i].getsuit() == 'Spades':
                Spades += 1
            if self.cards[i].getsuit() == 'Hearts':
                Hearts += 1
            if self.cards[i].getsuit() == 'Diamonds':
                Diamonds += 1
        if Clubs == 5 or Spades == 5 or Hearts == 5 or Diamonds == 5:
            return True
        return False

    def socreMountain(self):
        pass

    def scoreBackStraight(self):
        pass

    def scoreStraight(self):
        pass

    def scoreTriple(self):
        pass

    def scoreTwoPair(self):
        pass

    def scoreOnePair(self):
        pass

    def scoreTop(self):
        max = 0
        for i in range(7):
            if max < self.cards[i].getVaule():
                max = self.cards[i].getVaule()
        return max
