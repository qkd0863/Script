a, b = eval(input("두 정수를 입력하세요:"))


def f(a, b):
    if a % b == 0:
        print("최대공약수:",b)
    else:
        f(b, a % b)

f(a,b)
