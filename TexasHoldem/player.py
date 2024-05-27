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
        self.handhigh = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def getHandhigh(self):
        return self.handhigh

    def value(self):
        self.top = self.scoreTop()

        max = 0
        for i in range(2):
            if max < self.cards[i].getVaule():
                max = self.cards[i].getVaule()
        self.handhigh = max

        if self.scoreRoyalStraightFlush():
            return [self.ROYALSTAIGHTFLUSH, self.scoreTop()]

        if self.scoreBackStraightFlush():
            return [self.BACKSTAIGHTFLUSH, self.scoreTop()]

        if self.scoreStraightFlush():
            return [self.STRAIGHTFLUSH, self.high]

        if self.scoreFourCard():
            return [self.FOURCARD, self.high]

        if self.scoreFullHouse():
            return [self.FULLHOUSE, self.high]

        if self.scoreFlush():
            return [self.FLUSH, self.high]

        if self.scoreMountain():
            return [self.MOUNTAIN, self.scoreTop()]

        if self.scoreBackStraight():
            return [self.BACKSTAIGHT, self.scoreTop()]

        if self.scoreStraight():
            return [self.STRAIGHT, self.high]

        if self.scoreTriple():
            return [self.TRIPLE, self.high]

        if self.scoreTwoPair():
            return [self.TWOPAIR, self.high]

        if self.scoreOnePair():
            return [self.ONEPAIR, self.high]

        self.power = 'TOP'
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
                self.high = i
                return True
        return False

    def scoreFullHouse(self):
        index = [0] * 14
        Triple = False
        double = False
        tripleindex = 0
        doubleindex = 0
        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(1, 14):
            if index[i] == 3:
                Triple = True
                tripleindex = i
            if index[i] == 2:
                double = True
                doubleindex = i
        if Triple and double:
            m = max(tripleindex, doubleindex)
            if tripleindex == 1 or doubleindex == 1:
                m = 1
            self.power = "FullHouse"
            self.high = m
            return True
        return False

    def scoreFlush(self):
        Clubs = 0
        Spades = 0
        Hearts = 0
        Diamonds = 0
        max = 0
        for i in range(7):
            if self.cards[i].getsuit() == 'Clubs':
                Clubs += 1
            if self.cards[i].getsuit() == 'Spades':
                Spades += 1
            if self.cards[i].getsuit() == 'Hearts':
                Hearts += 1
            if self.cards[i].getsuit() == 'Diamonds':
                Diamonds += 1

        if Clubs == 5:
            self.power = "Flush"
            for i in range(7):
                if self.cards[i].getsuit() == 'Clubs' and self.cards[i].getVaule() == 1:
                    max = 1
                    break
                if self.cards[i].getsuit() == 'Clubs' and self.cards[i].getVaule() > max:
                    max = self.cards[i].getVaule()
            self.high = max
            return True

        if Spades == 5:
            self.power = "Flush"
            for i in range(7):
                if self.cards[i].getsuit() == 'Spades' and self.cards[i].getVaule() == 1:
                    max = 1
                    break
                if self.cards[i].getsuit() == 'Spades' and self.cards[i].getVaule() > max:
                    max = self.cards[i].getVaule()
            self.high = max
            return True

        if Hearts == 5:
            self.power = "Flush"
            for i in range(7):
                if self.cards[i].getsuit() == 'Hearts' and self.cards[i].getVaule() == 1:
                    max = 1
                    break
                if self.cards[i].getsuit() == 'Hearts' and self.cards[i].getVaule() > max:
                    max = self.cards[i].getVaule()
            self.high = max
            return True

        if Diamonds == 5:
            self.power = "Flush"
            for i in range(7):
                if self.cards[i].getsuit() == 'Diamonds' and self.cards[i].getVaule() == 1:
                    max = 1
                    break
                if self.cards[i].getsuit() == 'Diamonds' and self.cards[i].getVaule() > max:
                    max = self.cards[i].getVaule()
            self.high = max
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
        index = [0] * 14
        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(2, 10):
            if index[i] >= 1:
                if index[i + 1] >= 1 and index[i + 2] >= 1 and index[i + 3] >= 1 and index[i + 4] >= 1:
                    self.power = "Straight"
                    self.high = i + 4
                    return True
        return False

    def scoreTriple(self):
        index = [0] * 14
        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(1, 14):
            if index[i] == 3:
                self.power = "Triple"
                self.high = i
                return True
        return False

    def scoreTwoPair(self):
        index = [0] * 14
        count = 0
        pair = []

        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(1, 14):
            if index[i] == 2:
                pair.append(i)
                count += 1
        if count >= 2:
            self.power = "TwoPair"
            if 1 in pair:
                self.high = 1
            else:
                self.high = max(pair)
            return True
        return False

    def scoreOnePair(self):
        index = [0] * 14
        for i in range(7):
            index[self.cards[i].getVaule()] += 1
        for i in range(1, 14):
            if index[i] == 2:
                self.power = "OnePair"
                self.high = i
                return True
        return False

    def scoreTop(self):
        max = 0
        for i in range(7):
            if self.cards[i].getVaule() == 1:
                return 1
            if max < self.cards[i].getVaule():
                max = self.cards[i].getVaule()
        return max
