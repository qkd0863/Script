subtotal, rate = eval(input("소계와 팁 비율을 입력하세요"))
print("팁은 ", int(subtotal * rate) / 100, "이고 총액은 ", int(subtotal * rate) / 100 + subtotal, "입니다")
