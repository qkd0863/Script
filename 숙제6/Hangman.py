import random


def main():
    fp = open('hangman.txt')
    words = fp.read().split()
    while True:
        index = random.randint(0, len(words) - 1)
        hiddenword = words[index]
        guessword = ['*'] * len(hiddenword)
        NofCorrectChar = 0
        NofMiss = 0
        while NofCorrectChar < len(hiddenword):
            ch = input('(추측) 단어' + toString(guessword) + '에 포함되는 문자를 입력>')
            if ch in guessword:
                print('\tt', ch, '은 이미 포함되어 있습니다')
            elif hiddenword.find(ch) < 0:
                print(('\t', ch, '은 포함되어 있지 않습니다'))
                NofMiss += 1
            else:
                k = hiddenword.find(ch)
                while k >= 0:
                    guessword[k] = ch
                    NofCorrectChar += 1
                    k = hiddenword.find(ch, k + 1)
        print('정답은 ', hiddenword, '입니다', NofMiss, '번 실패했습니다')
        Yes = input("다른 단어 맞추기를 하시겠습니까? y/n")
        if Yes == 'n':
            break


def toString(guessword):
    result = ''
    for c in guessword:
        result += c
    return result


main()
