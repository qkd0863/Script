v = eval(input("10진수 입력:"))


def decimalToBinary(value):
    if value == 0:
        return ""
    else:
        if value % 16 == 10:
            r = 'A'
        elif value % 16 == 11:
            r = 'B'
        elif value % 16 == 12:
            r = 'C'
        elif value % 16 == 13:
            r = 'D'
        elif value % 16 == 14:
            r = 'E'
        elif value % 16 == 15:
            r = 'F'
        else:
            r = str(value % 16)
        return decimalToBinary(value // 16) + r


print("16진수:", decimalToBinary(v))
