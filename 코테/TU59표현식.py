In = input()

l = []
for i in In:
    if i == '+' or i == '-':
        b = l.pop()
        a = l.pop()

        c = '(' + a + i + b + ')'
        l.append(c)
    else:
        l.append(i)
print(l[0])