population = 312032486
sec = 60 * 60 * 24 * 365

for i in range(6):
    birth = (sec * i) // 7
    death = (sec * i) // 13
    immigrant = (sec * i) // 45
    future_population = population + birth - death + immigrant
    print(i, "년 뒤 인구:",
          future_population)
