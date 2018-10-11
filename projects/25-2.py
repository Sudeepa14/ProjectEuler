def fun(n):
    if n==1 or n==2:
        return(1)
    else:
        return(fun(n-1)+fun(n-2))
a=-1
n=0
while n>a:
    n+=1
    a+=1
    x=fun(n)
    y=str(x)
    if len(y)==1000:
        print(n)
        break
    
