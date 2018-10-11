l=[]
m=[]
for p in range(1,1001):
    s=0
    for i in range(1,p):
        for j in range(1,i):
            if p>i+j:
                s+=p
    l.append(p)
    m.append(s)
print(m.index(max(l)))
                
