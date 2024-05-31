import itertools


class Player:
    nomaid = 0
    Mangtong = 1
    kkeus = 2
    ttaeng = 3
    gwangttaeng = 4
    sampal = 5

    def __init__(self, name, num):
        self.playernum = num
        self.LCardPlayer = []
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
        if (self.maid()):
            pass
        else:
            return [self.nomaid, 0]

        if (self.scoreSampal()):
            return [self.sampal, self.scoreTop()]
        if (self.scoreGwangTTaeng()):
            return [self.gwangttaeng, self.scoreTop()]
        if (self.scoreTTaeng()):
            return [self.ttaeng, self.scoreTop()]
        if (self.scorekkeus()):
            return [self.kkeus, self.scoreTop()]
        if (self.scoreMangTong()):
            return [self.Mangtong, self.scoreTop()]

    def scoreSampal(self):
        combarr = self.getmaid()
        arr = []
        for i in range(5):
            arr.append(self.cards[i].getsuit())

        for i in range(len(combarr)):
            temparr = arr
            for j in range(3):
                temparr.remove(str(combarr[i][j]))

            if '3' in temparr or '8' in temparr:
                sam = False
                pal = False
                for k in range(5):
                    if (self.cards[k].getsuit() == '3' and self.cards[k].getVaule() == 1):
                        sam = True
                    if (self.cards[k].getsuit() == '8' and self.cards[k].getVaule() == 1):
                        pal = True
                if (sam and pal):
                    return True
        return False

    def scoreGwangTTaeng(self):
        pass

    def scoreTTaeng(self):
        pass

    def scorekkeus(self):
        pass

    def scoreMangTong(self):
        pass

    def scoreTop(self):
        pass

    def maid(self):
        arr = []
        for i in range(5):
            arr.append(int(self.cards[i].getsuit()))
        nCr = list(itertools.combinations(arr, 3))
        for i in range(len(nCr)):
            sum = 0
            for j in range(3):
                sum += nCr[i][j]
            if (sum == 10 or sum == 20):
                return True
        return False

    def getmaid(self):
        arr = []
        combarr = []
        for i in range(5):
            arr.append(int(self.cards[i].getsuit()))
        nCr = list(itertools.combinations(arr, 3))
        for i in range(len(nCr)):
            sum = 0
            for j in range(3):
                sum += nCr[i][j]
            if (sum == 10 or sum == 20):
                combarr.append(nCr[i])
        return combarr
