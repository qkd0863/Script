def f():
    x, y = eval(input("점의 x와 y 좌표값을 입력하세요."))
    if x > 200 or x < 0 or y > 100 or y < 0:
        print("외부")
    else:
        slope = -100 / 200
        y1 = y - slope * x
        if y1 <= 100:
            print("점은 삼각형의 내부에 있습니다.")
        else:
            print("점은 삼각형의 내부에 있지 않습니다.")

f()
f()