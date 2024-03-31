s = input("정수 리스트 입력:")
items = s.split()
numbers = [eval(x) for x in items]
numbers.reverse()
print("역순 리스트:", numbers)
