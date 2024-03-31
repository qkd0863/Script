def reverse(number):
    result = 0
    while number:
        rem = number % 10
        result = result * 10 + rem
        number //= 10
    return result



print(reverse(3456))
print(reverse(123456789))
