class Player:
    UPPER = 6
    LOWER = 7

    def __init__(self, name):
        self.name = name
        self.scores = [0 for i in range(self.UPPER + self.LOWER)]
        self.used = [False for i in range(self.UPPER + self.LOWER)]

    def setScore(self, score, index):
        self.scores[index] = score

    def setAtUsed(self, index):
        self.used[index] = True

    def getUpperScore(self):
        sum = 0
        for i in range(0, self.UPPER):
            sum += self.scores[i]
        return sum

    def getLowerScore(self):
        sum = 0
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            sum += self.scores[i]
        return sum

    def getUsed(self):
        return self.used

    def getTotalScore(self):
        sum1 = self.getUpperScore()
        sum2 = self.getLowerScore()
        return sum1 + sum2

    def toString(self):
        return self.name

    def allLowerUsed(self):
        for i in range(self.UPPER, self.UPPER + self.LOWER):
            if (self.used[i] == False):
                return False
            return True

    def allUpperUsed(self):
        for i in range(self.UPPER):
            if (self.used[i] == False):
                return False
            return True
