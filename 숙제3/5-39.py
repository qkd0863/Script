def f():
    sale = 1
    goal = 25000000
    commission = 0
    while commission < goal:
        sale += 1
        if sale > 10000000:
            commission = 5000000 * 0.08 + 5000000*0.1 + (sale - 10000000) * 0.12
        elif sale > 5000000:
            commission = 5000000 * 0.08 + (sale - 5000000) * 0.1
        else:
            commission = sale * 0.08
    print("최소 매출액:", sale)


f()
