v=[]
li=[]
def fun(n):
    l=0
    if n==1 :
        l+=1
        li.append(l)
        v.append(n)
        l=0
    elif n%2==0:
            n=n/2
            l+=1
            return(fun(n))
    else:
        n=n*3+1
        l+=1
        return(fun(n))

for n in range(2,2):
        fun(n)           
for x in li:
    if li[x]==max(li):
        print(v[x])
    
    
     
    
        
