import math
def distance(x1, y1, x2, y2):
    rx1 = math.radians(x1)
    rx2 = math.radians(x2)
    ry1 = math.radians(y1)
    ry2 = math.radians(y2)
    return 6370.01 * math.acos(math.sin(rx1) * math.sin(rx2) + math.cos(rx1) * math.cos(rx2) * math.cos(ry1 - ry2))

d1 = distance(35.1768201, 126.7735892, 37.7637326, 128.8824475)
d2 = distance(37.7637326, 128.8824475, 35.1645701, 129.0015892)
d3 = distance(37.565289, 126.8491259, 35.1645701, 129.0015892)

def area(d1, d2, d3):
    s = (d1 + d2 + d3) / 2
    return (s * (s - d1) * (s - d2) * (s - d3)) ** 0.5

area1 = area(d1, d2, d3)
print("서울-강릉-광주", area1)

d1 = distance(35.1645701, 129.0015892, 37.7637326, 128.8824475)
d2 = distance(35.1645701, 129.0015892, 35.1768201, 126.7735892)
d3 = distance(35.1768201, 126.7735892, 37.7637326, 128.8824475)
area2 = area(d1, d2, d3)
print("부산-강릉-광주", area2)

print("넓이:",
      area1 + area2)
