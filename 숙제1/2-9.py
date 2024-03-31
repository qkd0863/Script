temperature = eval(input("화씨 -58 와 41 사이의 온도를 입력하세요:"))
wind = eval(input("퓽속을 시간 당 마일 단위로 입력하세요:"))

perceived_temperature = 35.74 + 0.6215 * temperature - 35.75 * wind ** 0.16 + 0.4275 * temperature * wind ** 0.16

print("체감 온도는 ", perceived_temperature, "입니다")
