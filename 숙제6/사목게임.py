matrix = []


def drawBorad():
    for i in range(6):
        for j in range(7):
            print('|', matrix[i][j], end='')
        print('|')
    print("----------------------")


def check():
    for i in range(6):
        for j in range(4):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i][j + 1] and player == matrix[i][j + 2] and player == matrix[i][
                j + 3]:
                return player

    for i in range(3):
        for j in range(7):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i + 1][j] and player == matrix[i + 2][j] and player == matrix[i + 3][
                j]:
                return player

    for i in range(3):
        for j in range(4):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i + 1][j + 1] and player == matrix[i + 2][j + 2] and player == \
                    matrix[i + 3][j + 3]:
                return player

    for i in range(3):
        for j in range(4):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i + 1][j - 1] and player == matrix[i + 2][j - 2] and player == \
                    matrix[i + 3][j - 3]:
                return player

    return ''



def findRow(col):
    for row in range(5, -1, -1):
        if matrix[row][col] == ' ':
            return row
    return 6


def main():
    for i in range(6):
        matrix.append([])
        for j in range(7):
            matrix[i].append(' ')
    drawBorad()
    turn = True
    while True:
        if turn:
            col = eval(input("열 0-6에 빨간색 디스크를 떨어트리세요: "))
        else:
            col = eval(input("열 0-6에 노란색 디스크를 떨어트리세요: "))

        row = findRow(col)
        while True:
            if row != 6:
                if turn:
                    matrix[row][col] = 'R'
                else:
                    matrix[row][col] = 'Y'
                break
            else:
                print("꽉찬 열입니다. 다시 떨어트리세요")

        drawBorad()
        player = check()
        if player != '':
            if player == 'R':
                print("빨간색 플레이어가 이겼습니다")
            else:
                print("노란색 플레이어가 이겼습니다")
            break
        turn = not turn


main()
