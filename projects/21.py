n=0
q=0
y=0
p=0
li=[]
for i in  range(1,10000):
    for r in range(1,i):
        if i%r==0:
            n+=r
    for x in range(1,n):
        if n%x==0:
            y+=x
    if i==y and i!=n :
        p+=i+n
        q+=1
        li.append(i)
        li.append(n)
    n=0
    y=0
print(p/2)
        
            
    
        
        
