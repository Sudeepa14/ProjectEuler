q=1  
p=2
n=0
t=1
k=0
while p>q:
    p+=1
    q+=1
    n=0
    for i in range(2,p):
            if p%i!=0:
               n+=1
               if n==p-2:
                 n=0  
                 t+=1
                 if t==10001:
                     k=p
                     q=q+p
            else:
                continue
print(k)
