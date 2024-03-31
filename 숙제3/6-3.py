def reverse(number):
    result = 0
    while number:
        rem = number % 10
        result = result * 10 + rem
        number //= 10
    return result


def isPalindrome(number):
    return number == reverse(number)


print(isPalindrome(reverse(454)))
print(isPalindrome(reverse(45554)))

