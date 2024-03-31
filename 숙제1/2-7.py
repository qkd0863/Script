min = eval((input("분에 대한 숫자를 입력하세요")))

year_min = 60 * 24 * 365
day_min = 60 * 24

year = min // year_min
day = (min % year_min) // day_min
print(min, "분은 약", year, "년 ", day, "일 입니다")
