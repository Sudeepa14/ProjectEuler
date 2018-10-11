p=1
q=1
r=p+q
n=2
while r>p:
    p=q
    q=r
    r=p+q
    n+=1
    s=str(r)
    if len(s)==1000:
        r=p  
        print(n)
        break
