def func():
    numbers = input("정수들을 입력하세요:")
    list = [eval(i) for i in numbers.split()]
    d = {}
    for n in list:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    maxCount = max(d.values())
    print("가장 많이 나온 숫자:")
    for k, v in d.items():
        if v == maxCount:
            print(k, end=' ', )
    print()


func()