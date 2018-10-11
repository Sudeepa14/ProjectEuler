p=600851475143
n=0
l=0
for y in range(2,p):
    if p%y==0:
        n=0
        for i in range(2,y):
            if y%i!=0:
               n+=1
               if n==y-2:
                 n=0  
                 l=y
            else :
                continue
print(l)              

