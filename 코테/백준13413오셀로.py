T = eval(input())

for i in range(T):
    N = eval(input())
    BW = input()
    answer = input()
    NofBW = 0
    NofWB = 0
    for j in range(N):
        if BW[j] == 'B' and answer[j] == 'W':
            NofBW += 1
        elif BW[j] == 'W' and answer[j] == 'B':
            NofWB += 1
    print(max(NofBW, NofWB))