def compute(str):
    score = 0

    if str[1] == 'S' or str[1] == 'D' or str[1] == 'T':
        if str[1] == 'S':
            score += pow(int(str[0]), 1)
        if str[1] == 'D':
            score += pow(int(str[0]), 2)
        if str[1] == 'T':
            score += pow(int(str[0]), 3)

        if len(str) >= 3:
            if str[2] == '*':
                score *= 2
            if str[2] == '#':
                score *= -1

    else:
        if str[2] == 'S':
            score += pow(10, 1)
        elif str[2] == 'D':
            score += pow(10, 1)
        elif str[2] == 'T':
            score += pow(10, 1)

        if len(str) >= 4:
            if str[3] == '*':
                score *= 2
            if str[3] == '#':
                score *= -1

    return score


def solution(dartResult):
    answer = 0
    numindex = []
    flag = True
    score = []
    ex = []
    for i in range(len(dartResult)):
        if ord(dartResult[i]) >= ord('0') and ord(dartResult[i]) <= ord('9'):
            if flag == False:
                numindex.append(i)
            flag = True
        if not ord(dartResult[i]) >= ord('0') or not ord(dartResult[i]) <= ord('9'):
            flag = False



    ex.append(dartResult[0:numindex[0]])
    ex.append(dartResult[numindex[0]:numindex[1]])
    ex.append(dartResult[numindex[1]:])

    print(ex)
    for i in range(3):
        score.append(compute(ex[i]))
        for j in range(len(ex[i])):
            if i >= 1 and ex[i][j] == '*':
                score[i - 1] *= 2

    answer = score[0] + score[1] + score[2]

    return answer


solution('10S2D*3T')
