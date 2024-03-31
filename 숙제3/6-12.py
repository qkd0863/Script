def printChars(ch1, ch2, numberPerLine):
    count = 1
    for n in range(ord(ch1), ord(ch2) + 1):
        if count % numberPerLine == 0:
            print(chr(n))
        else:
            print(chr(n), end=' ')
        count += 1


printChars('1', 'Z', 10)
