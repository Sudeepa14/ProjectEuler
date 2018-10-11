def p(n):
    a=-1
    b=0
    s=0
    while s< n+1:
        a+=1
        b+=1
        for i in str(b):
           s+=1
           if s==n :
               q=int(i)
           
    return(q)
c=1
d=1
for e in range(1,8):
    c=10**(e-1)
    d*=p(c)
print(d)
