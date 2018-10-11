def fun(q):
    n=0
    l=0
    if q==2:
      return ('1')
    for i in range(2,q):
       if q%i!=0:
              n+=1
              if n==q-2:
                 n=0  
                 return ('1')
       elif q%i==0:
               return ('0')
               break
y =4 # below proggram wil not be identified circle primes under 10           
for z in range(1,1000001):
     
     if fun(z)=='1':
         a=str(z)
         b=list(a)
         x=1
         for i in range(1,len(b)):
             o=b[0]
             b.append(b[0])
             b.remove(b[0])
             t=0
             p=str(t)
             for h in b:
	              p+=h
             e=p[1:]            
             l=int(e)
             if fun(l)=='1':
                 x+=1
                 if x==len(b):
                     y+=1
print(y)                     



    
