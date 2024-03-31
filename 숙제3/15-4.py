def f(num):
    if num == 1:
        return 1
    return 1 / num + f(num - 1)


for i in range(1, 11):
    print("m({0})".format(i), f(i))
