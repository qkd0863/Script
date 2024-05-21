from Dice import *


class Configuration:
    configs = ["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
               "Upper Scores", "Upper Bonus(35)", "Three of a kind", "Four of a kind", "Full House(25)",
               "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance", "Lower Scores", "Total"]

    def getConfigs():
        return Configuration.configs

    def score(row, d):
        if (row >= 0 and row <= 6):
            return Configuration.scoreUpper(d, row + 1)
        elif (row == 8):
            return Configuration.scoreThreeOfAKind(d)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(d)
        elif (row == 10):
            return Configuration.scoreFullHouse(d)
        elif (row == 11):
            return Configuration.scoreSmallStraight(d)
        elif (row == 12):
            return Configuration.scoreLargeStraight(d)
        elif (row == 13):
            return Configuration.scoreYahtzee(d)
        elif (row == 14):
            return Configuration.sumDie(d)
        else:
            return -1

    def scoreUpper(d, num):
        sum = 0
        for i in range(5):
            if (d[i].getRoll() == num):
                sum += num
        return sum

    def scoreThreeOfAKind(d):
        index = [0] * 7
        for i in range(5):
            index[d[i].getRoll()] += 1

        for i in range(1, 7):
            if index[i] >= 3:
                return Configuration.sumDie(d)
        return 0

    def scoreFourOfAKind(d):
        index = [0] * 7
        for i in range(5):
            index[d[i].getRoll()] += 1

        for i in range(1, 7):
            if index[i] >= 4:
                return Configuration.sumDie(d)
        return 0

    def scoreFullHouse(d):
        index = [0] * 7
        double = False
        three = False
        for i in range(5):
            index[d[i].getRoll()] += 1
        for i in range(1, 7):
            if index[i] == 2:
                double = True
            if index[i] == 3:
                three = True
        if double and three:
            return 25
        else:
            return 0

    def scoreSmallStraight(d):
        s = set()
        if len(s) >= 4:
            if 1 in s and 2 in s and 3 in s and 4 in s:
                return 30
            if 2 in s and 3 in s and 4 in s and 5 in s:
                return 30
            if 3 in s and 4 in s and 5 in s and 6 in s:
                return 30
        return 0


    def scoreLargeStraight(d):
        s = set()
        for i in range(5):
            s.add(d[i].getRoll())
        if len(s) == 5:
            if 1 in s and 6 in s:
                return 0
            else:
                return 40
        else:
            return 0

    def scoreYahtzee(d):
        num = d[0].getRoll()
        for i in range(5):
            if (d[i].getRoll() != num):
                return 0
        return 50

    def sumDie(d):
        sum = 0
        for i in range(5):
            sum += d[i].getRoll()
        return sum
