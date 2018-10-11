p=1
q=2
t=0
while q>p:
    s=0
    p+=1
    q+=1
    for i in str(q):
        s+=int(i)**5
    if s==q:
        t+=s
        print(t)
