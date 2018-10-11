
def qu(n):
    global a
    a+=1
    if n%2==0:
        a+=1
        n=n/2
        if n==1:
            if  a!=1000000:
                 a=0
            else:
                print(q)
                p=q
        else:
         qu(n)
    else:
        
        n=3*n+1
        
        qu(n)


p=1
q=2
while q>p:
    p+=1
    q+=1
    n=q
    a=0
    qu(n)
