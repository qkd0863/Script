N = eval(input())

for i in range(N):
    ex = input()
    List = ex.split(' ')
    if List[1] == '*':
        if int(List[0]) * int(List[2]) == int(List[4]):
            print("correct")
        else:
            print("wrong answer")

    if List[1] == '-':
        if int(List[0]) - int(List[2]) == int(List[4]):
            print("correct")
        else:
            print("wrong answer")

    if List[1] == '+':
        if int(List[0]) + int(List[2]) == int(List[4]):
            print("correct")
        else:
            print("wrong answer")

    if List[1] == '/':
        if int(List[0]) / int(List[2]) == int(List[4]):
            print("correct")
        else:
            print("wrong answer")