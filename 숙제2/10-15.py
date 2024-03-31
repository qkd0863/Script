def isSorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


sList = input("정수를 입력:").split()
iList = [eval(i) for i in sList]

if isSorted(iList):
    print("정렬되어 있음")
else:
    print("정렬되어 있지 않음")


sList = input("정수를 입력:").split()
iList = [eval(i) for i in sList]

if isSorted(iList):
    print("정렬되어 있음")
else:
    print("정렬되어 있지 않음")
