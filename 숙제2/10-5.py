s = input("10 개의 숫자를 입력하세요:")
items = s.split()
list1 = [eval(x) for x in items]

list2 = []
for num in list1:
    if not num in list2:
        list2.append(num)

print("중복을 제거한 고유한 숫자", list2)
