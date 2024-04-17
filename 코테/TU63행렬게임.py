A, B = map(eval, input().split())

maxtrix = []
for i in range(A):
    maxtrix.append([])
    for j in range(1, B + 1):
        maxtrix[i].append(B * i + j)

print('M')
for i in range(A):
    for j in range(B):
        print(maxtrix[i][j], end='')
        if j != B - 1:
            print(" ", end='')
    print()

print('R')
for j in range(B):
    for i in range(A - 1, -1, -1):
        print(maxtrix[i][j], end='')
        if i != 0:
            print(" ", end='')
    print()

print('L')
for j in range(B - 1, -1, -1):
    for i in range(A):
        print(maxtrix[i][j], end='')
        if i != A - 1:
            print(" ", end='')

    print()

print('T')
for j in range(B):
    for i in range(A):
        print(maxtrix[i][j], end='')
        if i != A - 1:
            print(" ", end='')
    if j != B - 1:
        print()
