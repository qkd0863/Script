def reverse(number):
    result = 0
    while number:
        rem = number % 10
        result = result * 10 + rem
        number //= 10
    return result


def isPalindrome(number):
    return number == reverse(number)


def prime(number):
    n = 2
    while (n < number ** 0.5 + 1):
        if number % n == 0:
            return False
        n += 1
    return True


num = eval(input())
while True:
    if isPalindrome(num) and prime(num):
        print(num)
        break
    num += 1