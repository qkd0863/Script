import random

def f():
    count = 0
    for i in range(1000000):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if x < 0:
            count += 1
        elif 0 <= x <= 1 and 0 <= y <= 1:
            slope = -1
            y1 = y - slope * x
            if y1 <= 1:
                count += 1
    print("확률:", count / 1000000)

f()
f()
f()