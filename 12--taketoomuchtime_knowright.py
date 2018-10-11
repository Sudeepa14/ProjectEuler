p=0
q=1
r=1
n=2
t=1
while q>p:
    p+=1
    q+=1
    r+=q
    n=2
    for i in range(2,r):
        if r%i==0:
            n+=1
        if n>6:
             t=0
    if t==0:
        print(r)
        n=2
        break
