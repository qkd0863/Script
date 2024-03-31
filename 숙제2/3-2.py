import math

x1, y1 = eval(input("첫 번째 점(위도와 경도)을 60분법 각으로 입력하세요:"))
x2, y2 = eval(input("두 번째 점(위도와 경도)을 60분법 각으로 입력하세요:"))

rx1 = math.radians(x1)
rx2 = math.radians(x2)
ry1 = math.radians(y1)
ry2 = math.radians(y2)

d = 6370.01 * math.acos(math.sin(rx1) * math.sin(rx2) + math.cos(rx1) * math.cos(rx2) * math.cos(ry1 - ry2))
print("두 점 사이의 거리는", d, "km 입니다")
