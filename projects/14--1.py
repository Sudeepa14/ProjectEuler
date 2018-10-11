p=2
n=1
def check(x):
    n+=1
    if x%2==0:
        return(x==x/2)
    else:
        return(x==3*x+1)
for x in range(2,1000001):
    while x==1:
      y=check(x)
    if n>p:
     p=n
    
    
    
    
