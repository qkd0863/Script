from itertools import combinations

N = eval(input())
foodList = []

for i in range(N):
    foodList.append([eval(s) for s in input().split()])

tan, dan, ge, yel = map(eval, input().split())
count = 0

for num in range(1,4):
    for i in combinations(foodList, num):
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        for j in range(len(i)):
            temp1 += i[j][0]
            temp2 += i[j][1]
            temp3 += i[j][2]
            temp4 += i[j][0] * 4 + i[j][1] * 4 + i[j][2] * 9
        if temp1 > tan:
            continue
        if temp2 < dan:
            continue
        if temp3 > ge:
            continue
        if temp4 > yel:
            continue
        count += 1


print(count)
