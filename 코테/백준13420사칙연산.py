T = eval(input())

for i in range(T):
    H, W, N = map(eval, input().split())

    if N % H == 0:
        answer = H * 100 + (N // H)
    else:
        answer = (N % H) * 100 + (N // H) + 1

    print(answer)
