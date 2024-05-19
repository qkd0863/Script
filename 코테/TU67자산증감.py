N = eval(input())
List = input()

matrix = []
level = 99
for i in range(200):
    matrix.append([])

for i in range(N):
    check = 0
    for j in range(200):
        if j != level:
            matrix[j].append('.')
        else:
            if i == N - 1:
                if List[i] == '+':
                    matrix[j].append('/')
                if List[i] == '-':
                    matrix[j].append('\\')
                if List[i] == '=':
                    matrix[j].append('_')
                continue

            if List[i] == '+' and List[i + 1] != '-':
                matrix[j].append('/')
                check = 1
            elif List[i] == '+' and List[i + 1] == '-':
                matrix[j].append('/')

            if List[i] == '-' and List[i + 1] == '-':
                matrix[j].append('\\')
                check = 2
            elif List[i] == '-' and List[i + 1] != '-':
                matrix[j].append('\\')

            if List[i] == '=':
                matrix[j].append('_')
                if List[i + 1] == '-':
                    check = 2

    if check == 1:
        level -= 1
    if check == 2:
        level += 1

i = 0
while i < len(matrix):
    if '\\' in matrix[i]:
        i += 1
        continue
    if '/' in matrix[i]:
        i += 1
        continue
    if '_' in matrix[i]:
        i += 1
        continue
    del matrix[i]

for i in range(len(matrix)):
    for j in range(N):
        print(matrix[i][j], end='')
    print()
