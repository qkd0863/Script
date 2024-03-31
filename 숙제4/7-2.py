class Stock:

    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol
    def getP(self):
        return self.__previousClosingPrice
    def getC(self):
        return self.__currentPrice

    def setP(self,previousClosingPrice):
        self.__previousClosingPrice=previousClosingPrice
    def setC(self,currentPrice):
        self.__currentPrice=currentPrice

    def getChangePercent(self):
        return (self.__currentPrice-self.__previousClosingPrice)/self.__previousClosingPrice*100



s=Stock("INTC","Intel Corporation",20500,20350)

print(s.getChangePercent())


