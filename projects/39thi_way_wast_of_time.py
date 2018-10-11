l2=[]
l1=[]
n=0
for p in range(1,999):
    for q in range(1,p):
        for r in range(1,p):
            if p+q+r<1001:
                
            if p**2==q**2+r**2:
                  n+=1
    if n>1:
            l1.append(p)
            l2.append(n)
    n=0        
for i in l2:
    if l2[i]==max(l2):
        print(l1[i])
