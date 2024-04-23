count=0
flag=True
for i in range(8):
    B=input()
    for j in range(8):
        if flag:
            if j%2==0 and B[j]=='F':
                count+=1
        else:
            if j%2==1 and B[j]=='F':
                count +=1
    flag=not flag
print(count)