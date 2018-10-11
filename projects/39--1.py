l1=[]
l=[]
m=[]
n=0
for p in range(1,1001):
    l1.append(p)
for i in l1:
    for j in l1:
         a=1000-(i+j)
         if a>0:
            for k in l1:
                if k==a :
                    if i**2==j**2 +k**2:
                        n+=1
    if n>1:
       l.append(i)
       m.append(n)
for g in m:
    if m[g]==max(m):
        print(l[g])

                           
                    
