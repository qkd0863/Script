s = input("1과 100사이의 정수를 입력하세요:")
sList = s.split()
iList = [eval(i) for i in sList]

histogram = [0] * 100
for i in iList:
    histogram[i - 1] += 1

for i in range(100):
    if histogram[i]:
        print(i + 1, "-", histogram[i], "번 나타납니다.")
