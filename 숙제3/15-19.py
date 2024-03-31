v = eval(input("10진수 입력:"))


def decimalToBinary(value):
    if value == 0:
        return ""
    else:
        return decimalToBinary(value // 2) + str(value % 2)


print("이진수:", decimalToBinary(v))
