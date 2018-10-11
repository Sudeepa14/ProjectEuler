import math
p=1
q=2
h=0
t=0
k=0
while q>p:
    p+=1
    q+=1
    if q%2==1:
        for i in range(2,q):
          ####################starting prime
          y=i
          n=0
          l=0
          if y==2:
            k=1
          for i in range(2,y):
              if y%i!=0:
                 n+=1
                 if n==y-2:
                  n=0
                  k=1
                 
              elif y%i==0:
               k=0
               break
          ###################ending primes
          if k==1 and math.sqrt((q-i)/2)==int(math.sqrt((q-i)/2)):
                t=1
                break
        if t==1:
             print(q)
        t=0


  
          















        
