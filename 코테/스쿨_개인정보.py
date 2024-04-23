def to_days(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    D = {}
    for s in terms:
        key = s[0]
        value = eval(s[2:])
        D[key] = value

    Today = to_days(today)
    answer = []

    for i, privacy in enumerate(privacies):
        if Today >= to_days(privacy[:10]) + D[privacy[11]] * 28:
            answer.append(i + 1)

    return answer