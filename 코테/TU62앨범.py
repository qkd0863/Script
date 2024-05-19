N = eval(input())

Dict = {}
Genre = []
for i in range(N):
    genre, play = input().split()
    play = eval(play)
    if genre in Dict:
        Dict[genre][0] += play
        if Dict[genre][1][1] < play:
            Dict[genre][2] = Dict[genre][1]
            Dict[genre][1] = (i, play)
        elif Dict[genre][2][1] < play:
            Dict[genre][2] = (i, play)
    else:
        Dict[genre] = [play, (i, play), (-1, 0)]


for genre, value in Dict.items():
    Genre.append((genre, value[0]))

Genre.sort(key=lambda x: x[1], reverse=True)
for i in range(len(Genre)):
    print(Dict[Genre[i][0]][1][0])
    if Dict[Genre[i][0]][2][0] != -1:
        print(Dict[Genre[i][0]][2][0])

