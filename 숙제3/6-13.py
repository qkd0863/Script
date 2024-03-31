def m(n):
    if n==1:
        return 1/2
    return  m(n-1)+n/(n+1)

for i in range(1,21):
    print(i,'\t',m(i))

