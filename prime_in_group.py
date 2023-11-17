num=(3,4,5,6,7)
for a in num:
    c=int(a)
    t=0
    for x in range (2,c):
        if c%x==0:
            t=1
            break
    if t==0:
        print(c)
