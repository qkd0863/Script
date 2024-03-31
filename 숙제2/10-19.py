import random

b = eval(input("떨어뜨릴 공의 개수를 입력하세요:"))
s = eval(input("콩 기계의 슬롯 개수를 입력하세요:"))

slots = [0] * s

for ball in range(b):
    nofR = 0
    for slot in range(s - 1):
        if random.random() > 0.5:
            print("R", end='')
            nofR += 1
        else:
            print("L", end='')
    slots[nofR] += 1
    print()

print(slots)
Max = max(slots)
for h in range(Max, 0, -1):
    for i in range(s):
        if slots[i] >= h:
            print("0", end='')
        else:
            print(" ", end='')
    print()
