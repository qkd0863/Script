N = eval(input())

for i in range(N):
    matrix = []
    for j in range(13):
        temp = input()
        index = 0
        if j >= 1 and j <= 3:
            count = [0] * 10
            matrix.append(temp)
            for k in range(13):
                if matrix[j][k].isdigit():
                    count[matrix[j][k]]+=1

            for i in range(10):
                if count[i]>1:
                    print('N')
                    break
