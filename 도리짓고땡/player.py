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
        self.betMoney = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self):
        if (not self.maid()):
            return [self.nomaid, [0, 0]]

        num = self.scorekkeus()
        if (self.scoreSampal()):
            return [self.sampal, num]
        if (self.scoreGwangTTaeng()):
            return [self.gwangttaeng, num]
        if (self.scoreTTaeng()):
            return [self.ttaeng, num]

        if num[0] > 0:
            return [self.kkeus, num]
        else:
            return [self.Mangtong, num]

    def scoreSampal(self):
        val_arr = self.getmaid()
        sam = False
        pal = False
        for i in range(5):
            if self.cards[i].getVaule() == 1 and self.cards[i].getsuit() == 3:
                sam = True
            if self.cards[i].getVaule() == 1 and self.cards[i].getsuit() == 8:
                pal = True

        if (not sam or not pal):
            return False

        for i in range(len(val_arr)):
            if 3 in val_arr[i] and 8 in val_arr[i]:
                return True
        return False

    def scoreGwangTTaeng(self):
        val_arr = self.getmaid()

        ill = False
        sam = False
        pal = False
        for i in range(5):
            if self.cards[i].getVaule() == 1 and self.cards[i].getsuit() == 1:
                ill = True
            if self.cards[i].getVaule() == 1 and self.cards[i].getsuit() == 3:
                sam = True
            if self.cards[i].getVaule() == 1 and self.cards[i].getsuit() == 8:
                pal = True

        if not ill:
            return False

        if (not sam and not pal):
            return False

        for i in range(len(val_arr)):
            if 1 in val_arr[i] and 3 in val_arr[i]:
                return True
            if 1 in val_arr[i] and 8 in val_arr[i]:
                return True
        return False

    def scoreTTaeng(self):
        val_arr = self.getmaid()
        for i in range(len(val_arr)):
            if val_arr[i][0] == val_arr[i][1]:
                return True
        return False

    def scorekkeus(self):
        val_arr = self.getmaid()
        sum = [0, [0, 0]]
        for i in range(len(val_arr)):
            if (sum[0] <= (val_arr[i][0] + val_arr[i][1]) % 10):
                sum[0] = (val_arr[i][0] + val_arr[i][1]) % 10
                sum[1][0] = val_arr[i][0]
                sum[1][1] = val_arr[i][1]

        return sum

    def maid(self):
        arr = []
        for i in range(5):
            arr.append(self.cards[i].getsuit())
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
            arr.append(self.cards[i].getsuit())
        nCr = list(itertools.combinations(arr, 3))
        for i in range(len(nCr)):
            sum = 0
            for j in range(3):
                sum += nCr[i][j]
            if (sum == 10 or sum == 20):
                combarr.append(nCr[i])

        val_arr = []

        for i in range(len(combarr)):
            temparr = arr[:]
            for j in range(3):
                temparr.remove(combarr[i][j])

            val_arr.append(temparr)

        return val_arr
