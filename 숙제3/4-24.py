import random

carddeck = [i for i in range(52)]
random.shuffle(carddeck)
suit = ["스페이드", "다이아몬드", "하트", "클로버"]
numbers = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

for number in carddeck:
    quot = number // 13
    print(suit[quot], end='')
    rem = number % 13
    print(numbers[rem])