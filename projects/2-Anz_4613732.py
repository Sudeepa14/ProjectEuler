p=1
q=2
r=p+q
s=2
while r<4000001:
    p=q
    q=r
    r=p+q
    if r%2==0:
        s+=r   
print(s)    
