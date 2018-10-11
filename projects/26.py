l=[]
for d in range(1,1000):
    n=1
    p=1/d
    s=p*10**n-p**(n+1)
    while str(s)[2:]==0:
     n+=1
     l.append(d)
print(max(l))
