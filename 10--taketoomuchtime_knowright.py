s=2
n=0
for p in range(2,2000000):
    n=0
    for i in range(2,p):
            if p%i==0:
                continue
               
            else :
                n+=1
                if n==p-2:
                 print(p)
                 n=0  
                 s+=p
print(s)              
