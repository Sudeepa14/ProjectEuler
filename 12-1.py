p=0
q=1
r=1
n=2
t=1


while n<501:
    p+=1
    q+=1
    r+=q
    for i in range(2,r):
        if r%i==0:
            n+=1
            
print(r)          
