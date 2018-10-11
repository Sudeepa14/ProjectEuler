s=2
n=0
for p in range(1,2000000):
    n=0
    for i in range(2,p):
            if p%i!=0:
               n+=1
               if n==p-2:
                 n=0  
                 s+=p
            else :
                continue
print(s)              
