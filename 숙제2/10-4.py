s = input("정수를 입력:")
sList = s.split()
iList = [eval(i) for i in sList]
average = sum(iList) / len(iList)
count = 0
for i in iList:
    if i > average:
        count += 1

print("평균 이상 점수 개수:", count)
print("평균 미만 점수 개수:", len(iList) - count)
