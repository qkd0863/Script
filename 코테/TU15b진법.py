[b, N, M] = [eval(s) for s in input().split()]
Nlist = [eval(s) for s in input().split()]
Mlist = [eval(s) for s in input().split()]


def BtoDec(L, b):
    result = 0
    for i in L:
        result = result * b + i
    return result


num1 = BtoDec(Nlist, b)
num2 = BtoDec(Mlist, b)
P = num1 * num2
Plist = []
while P:
    Plist.insert(0, P % b)
    P //= b

print(len(Plist))
for i in Plist:
    print(i, end=" ")
print()

