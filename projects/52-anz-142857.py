p=1
q=2
while q>p:
    q+=1
    p+=1
    a=list(str(q))
    b=list(str(2*q))
    c=list(str(3*q))
    d=list(str(4*q))
    e=list(str(5*q))
    f=list(str(6*q))
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    e.sort()
    f.sort()
    if a==b==c==d==e==f==e==f:
        print(q)
        break
    
