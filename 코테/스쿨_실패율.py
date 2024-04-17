def solution(N, stages):
    answer = []
    counts = [0 for i in range(500)]
    comp = []
    challenge = len(stages)
    for i in range(len(stages)):
        counts[stages[i]] += 1

    for i in range(1, N + 1):
        if challenge != 0:
            fail = counts[i]
            comp.append(fail / challenge, i)
            challenge -= fail
        else:
            comp.append([0, i])

    comp.sort(key=lambda x: -x[0][0])

    for i in range(len(comp)):
        answer.append(comp[1])

    return answer



def solution(N, stages):
    answer = []
    arr = []
    len_s = len(stages)

    for i in range(N):
        if len_s!=0:
            a = stages.count(i+1)
            arr.append((i+1,a/len_s))
            len_s -= a
        else:
            arr.append((i+1,0))
    arr.sort(key=lambda x:-x[1])

    for a in arr:
        answer.append(a[0])
    return answer