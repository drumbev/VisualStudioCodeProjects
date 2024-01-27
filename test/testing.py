c = 0
for i in range(100000, 1000000):
    ch=0
    nech=0
    s = str(i)
    for j in s:
        if int(j)%2==0:
            ch+=1
        else:
            nech+=1
    if ch==nech:
        c+=1
        if i%10000==0:
            print(i)
        
print(c)
print('jk')