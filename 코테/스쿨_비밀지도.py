def transform(arr, n):
    temp = []
    for i in range(n):
        a = "{0:b}".format(arr[i]).zfill(n)
        temp.append(a)
    return temp


def solution(n, arr1, arr2):
    answer = []
    map1 = transform(arr1, n)
    map2 = transform(arr2, n)

    for i in range(n):
        s = ""
        for j in range(n):
            if map1[i][j] == '1':
                s += '#'
                continue
            if map2[i][j] == '1':
                s += '#'
                continue
            s += ' '
        answer.append(s)

    return answer


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        s = str(bin(i | j)[2:])

        s = s.zfill(n)
        print(s)
        s = s.replace('1', '#')
        s = s.replace('0', ' ')
        answer.append(s)

    return answer
