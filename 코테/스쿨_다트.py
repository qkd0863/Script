def compute(str):
    score = 0
    num = 0
    index = 0
    for i in range(len(str)):
        if not ord(str[i]) >= ord('0') or not ord(str[i]) <= ord('9'):
            num = str[:i]
            index = 0
            break
    num=eval(num)
    for i in range(index, len(str)):
        if str[i] == 'S':
            score += num
        if str[i] == 'D':
            score += pow(num, 2)
        if str[i] == 'T':
            score += pow(num, 3)
        if str[i] == '*':
            score *= 2
        if str[i] == '#':
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
