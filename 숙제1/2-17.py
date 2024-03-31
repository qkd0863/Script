weight = eval((input("몸무게를 파운드로 입력하세요")))
height = eval((input("키를 인치로 입력하세요")))

kg_weight = weight * 0.45359237
m_height = height * 0.0254
BMI = kg_weight / m_height ** 2
print("BMI는 ", BMI, "입니다")
