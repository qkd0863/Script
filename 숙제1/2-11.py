money = eval(input("약정 금액을 입력하세요:"))
year_interest = eval(input("연이율(%)을 입력하세요:"))
year = eval(input("약정 기간(년)을 입력하세요:"))

month_payment = money / (1 + (year_interest / 1200)) ** (year * 12)
print("월 납입금은 ", month_payment, "입니다")
