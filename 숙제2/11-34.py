numbers = input("6개의 점을 입력하세요:")
list = [eval(i) for i in numbers.split()]

def getRightmostLowestPoint(points):
    min = points[1]
    max = 0
    for num in range(0, len(points), 2):
        if points[num] > 0:
            if points[num + 1] < min:
                min = points[num + 1]
    for i in range(0, len(points)):
        if points[i] == min:
            d = points[i - 1] ** 2 + points[i] ** 2
            if max < d:
                max = d
    for j in range(0, len(points), 2):
        if points[j] ** 2 + points[j + 1] ** 2 == max:
            return points[j], points[j + 1]


print("최우측하단의 점은:", getRightmostLowestPoint(list))
