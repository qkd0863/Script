num = eval(input("0과 1000사이의 숫자를 입력하세요:"))

a = num // 100
b = (num // 10) % 10
c = (num % 100) % 10

print("이 자릿수들의 합은 ", a + b + c, "입니다")
