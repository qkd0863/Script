List = input()
bomb = input()

while List.find(bomb) != -1:
    List = List.replace(bomb, '')

print(List)
