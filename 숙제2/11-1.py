def func():
    maxtrix = []
    for i in range(3):
        s = input("3 X 4 행렬의 행 {0} 번에 대한 원소를 입력하세요".format(i))
        l = [eval(i) for i in s.split()]
        maxtrix.append(l)
    for j in range(4):
        print("열 {0}번 원소의 총합은 {1} 입니다.".format(j, sumColumn(maxtrix, j)))


def sumColumn(m, columnindex):
    sum = 0
    for i in range(len(m)):
        sum += m[i][columnindex]
    return sum


func()
