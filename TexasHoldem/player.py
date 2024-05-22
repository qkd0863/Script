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
        self.power = ""
        self.top = 0
        self.high = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self):
        self.top = self.scoreTop()

        if self.scoreRoyalStraightFlush():
            return [self.ROYALSTAIGHTFLUSH, self.scoreTop()]

        if self.scoreBackStraightFlush():
            return [self.BACKSTAIGHTFLUSH, self.scoreTop()]

        if self.scoreStraightFlush():
            return [self.STRAIGHTFLUSH, self.scoreTop()]

        if self.scoreFourCard():
            return [self.FOURCARD, self.scoreTop()]

        if self.scoreFullHouse():
            return [self.FULLHOUSE, self.scoreTop()]

        if self.scoreFlush():
            return [self.FLUSH, self.scoreTop()]

        if self.scoreMountain():
            return [self.MOUNTAIN, self.scoreTop()]

        if self.scoreBackStraight():
            return [self.BACKSTAIGHT, self.scoreTop()]

        if self.scoreStraight():
            return [self.STRAIGHT, self.scoreTop()]

        if self.scoreTriple():
            return [self.TRIPLE, self.scoreTop()]

        if self.scoreTwoPair():
            return [self.TWOPAIR, self.scoreTop()]

        if self.scoreOnePair():
            return [self.ONEPAIR, self.scoreTop()]

        self.power='TOP'
        return [self.TOP, self.scoreTop()]

    def scoreRoyalStraightFlush(self):
        card = []
        for i in range(7):
            card.insert(i, [self.cards[i].getsuit(), self.cards[i].getVaule()])
        if 10 in card and 11 in card and 12 in card and 13 in card and 1 in card:
            if self.scoreFlush():
                self.power = "RoyalStraightFlush"
                return True
        else:
            return False

    def scoreBackStraightFlush(self):
        card = []
        for i in range(7):
            card.insert(i, [self.cards[i].getsuit(), self.cards[i].getVaule()])
        if 1 in card and 2 in card and 3 in card and 4 in card and 5 in card:
            if self.scoreFlush():
                self.power = "BackStraightFlush"
                return True
        else:
            return False

    def scoreStraightFlush(self):
        if self.scoreFlush():
            if self.scoreStraight():
                self.power = "Straight"
                return True
        return False

    def scoreFourCard(self):
        index = [0] * 14
        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(1, 14):
            if index[i] == 4:
                self.power = "FourCard"
                return True
        return False

    def scoreFullHouse(self):
        index = [0] * 14
        Triple = False
        double = False
        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(1, 14):
            if index[i] == 3:
                Triple = True
            if index[i] == 2:
                double = True
        if Triple and double:
            self.power = "FullHouse"
            return True
        return False

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
            self.power = "Flush"
            return True
        return False

    def scoreMountain(self):
        card = []
        for i in range(7):
            card.insert(i, self.cards[i].getVaule())
        if 10 in card and 11 in card and 12 in card and 13 in card and 1 in card:
            self.power = "Mountain"
            return True
        return False

    def scoreBackStraight(self):
        card = []
        for i in range(7):
            card.insert(i, self.cards[i].getVaule())
        if 1 in card and 2 in card and 3 in card and 4 in card and 5 in card:
            self.power = "BackStraight"
            return True
        return False

    def scoreStraight(self):
        card = []
        for i in range(7):
            card.insert(i, self.cards[i].getVaule())
        if max(card) - min(card) == 4:
            self.power = "Straight"
            return True
        return False

    def scoreTriple(self):
        index = [0] * 14
        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(1, 14):
            if index[i] == 3:
                self.power = "Triple"
                return True
        return False

    def scoreTwoPair(self):
        index = [0] * 14
        count = 0
        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(1, 14):
            if index[i] == 2:
                count += 1
        if count >= 2:
            self.power = "TwoPair"
            return True
        return False

    def scoreOnePair(self):
        index = [0] * 14
        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(1, 14):
            if index[i] == 2:
                self.power = "OnePair"
                return True
        return False

    def scoreTop(self):
        max = 0
        for i in range(7):
            if max < self.cards[i].getVaule():
                max = self.cards[i].getVaule()
        return max
