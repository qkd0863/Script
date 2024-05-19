N, K = map(eval, input().split())

for _ in range(K):
    L = [eval(s) for s in input().split()]
    for i in range(N - 1, 0, -1):
        if L[i - 1] < L[i]:
            R = L[i - 1:]
            R.sort()
            index = R.index(L[i - 1])
            next = R[index + 1]
            R.pop(index + 1)
            R.insert(0, next)
            L = L[:i - 1] + R
            break
    for n in L:
        print(n, end=' ')
    print()