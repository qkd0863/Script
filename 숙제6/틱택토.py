matrix = []


def drawBorad():
    for i in range(3):
        print("----------")
        for j in range(3):
            print('|', matrix[i][j], end='')
        print('|')
    print("----------")


def check():
    for i in range(3):
        player = matrix[i][0]
        if player != ' ' and player == matrix[i][1] and player == matrix[i][2]:
            return player

        player = matrix[0][i]
        if player != ' ' and player == matrix[i][1] and player == matrix[i][2]:
            return player

    player = matrix[0][0]
    if player != ' ' and player == matrix[1][1] and player == matrix[2][2]:
        return player
    player = matrix[0][2]
    if player != ' ' and player == matrix[1][1] and player == matrix[2][0]:
        return player
    return ' '


def main():
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(' ')
    drawBorad()
    turn = True
    for i in range(9):
        if turn:
            row = eval(input("플레이어의 x의 행 입력: "))
            col = eval(input("플레이어의 y의 행 입력: "))
            matrix[row][col] = 'X'
        else:
            row = eval(input("플레이어의 x의 행 입력: "))
            col = eval(input("플레이어의 y의 행 입력: "))
            matrix[row][col] = 'O'
        drawBorad()
        player = check()
        if player != ' ':
            print("플레이어", player, '가 이겼습니다')
            break
        turn = not turn
        if i == 9:
            print("비겼습니다")


main()
