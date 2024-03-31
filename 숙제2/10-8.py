s = input("정수 리스트 입력:")
items = s.split()
list = [eval(x) for x in items]


def indexOfSmallestElement(lst):
    min = lst[0]
    index = 0
    for i in range(1, len(lst)):
        if min > lst[i]:
            min = lst[i]
            index = i
    return index


print("가장 작은 정수의 인덱스:", indexOfSmallestElement(list))
