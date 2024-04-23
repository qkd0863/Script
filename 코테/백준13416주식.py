T = eval(input())

for i in range(T):
    N = eval(input())
    money = 0
    for j in range(N):
        l = [eval(s) for s in input().split()]

        if max(l) > 0:
            money += max(l)
    print(money)
