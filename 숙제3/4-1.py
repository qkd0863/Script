
def f():
    a, b, c = eval(input("A, B, C를 입력하세요:"))
    D = b ** 2 - 4 * a * c

    r1 = (-b + D ** 0.5) / (2 * a)
    r2 = (-b - D ** 0.5) / (2 * a)

    if D > 0:
        print("실근은 {0}, {1} 입니다".format(r1, r2))
    elif D == 0:
        print("실근은 {0} 입니다".format(r1))
    else:
        print("이 방정식은 실근이 존재하지 않습니다")


f()
f()
f()
