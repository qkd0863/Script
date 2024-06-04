class Card:
    def __init__(self, number):
        self.x = number // 4
        self.value = number % 4 + 1

    def getsuit(self):
        suits = []
        for i in range(1, 11):
            suits.append(i)
        return suits[self.x]

    def filename(self):
        return str(self.getsuit()) + "." + str(self.value) + '.gif'

    def getVaule(self):
        return self.value
