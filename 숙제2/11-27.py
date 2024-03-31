def func():
    maxtrix = []
    for i in range(3):
        numbers = input("3 X 3 행렬을 한 행씩 입력하세요")
        list = [eval(i) for i in numbers.split()]
        maxtrix.append(list)
    sortColums(maxtrix)


def sortColums(m):
    for k in range(3):
        for i in range(3):
            for j in range(0, 3 - i - 1):
                if m[j][k] > m[j + 1][k]:
                    m[j][k], m[j + 1][k] = m[j + 1][k], m[j][k]
    print("열 정렬된 리스트는 다음과 같습니다.")
    for num in range(3):
        print(m[num])


func()
