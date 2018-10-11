p=1
q=1
r=p+q
n=2
s=str(r)
t=len(s)
while t<1001 :
    p=q
    q=r
    r=p+q
    n+=1
print(n)    
