a, b, c = eval(input("세 개의 수를 입력하세요:"))


def displaySortedNumbers(num1, num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1
    print("정렬된 숫자는", num1, num2, num3)

displaySortedNumbers(a,b,c)