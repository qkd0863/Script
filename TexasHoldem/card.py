class Card:
    def __init__(self,number):
        self.x=number//13
        self.value=number%13+1
    def getsuit(self):
        suits=['Clubs','Spades','Hearts','Diamonds']
        return suits[self.x]
    def filename(self):
        return self.getsuit()+str(self.value)+'.png'
    def getVaule(self):
        if self.value>10:
            return 10
        else:
            return self.value