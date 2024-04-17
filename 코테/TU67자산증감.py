N = eval(input())
List = input()

state = 0
low = 0
high = 0
level = 0

for i in range(len(List)):
    if List[i] == '+':
        state += 1
    if List[i] == '-':
        state -= 1


    if low > state:
        low = state
    if high < state:
        high = state
print(low, high)

M = abs(low) + abs(high)


matrix = []
for i in range(M):
    matrix.append([])

for i in range(len(List)):
    for j in range(M):
        matrix[j].append('.')

for i in range(M):
    for j in range(len(List)):
        print(matrix[i][j], end='')
    print()
