p=0
q=1
l1=[]
l2=[]
import time
start=time=time.time()

if time.time ()==900:
    p=q
 





while q>p:
    p+=1
    q+=1
    l1.append(q)
    t=0
    for i in l1:
        for  j in l1:
            if not i==j:
                t+=1
    if t == len(l1)**2:
         y=q
         n=0
         l=0
         if y==2:
          l2.append(q)
         for i in range(2,y):
             if y%i!=0:
                       n+=1
                       if n==y-2:
                          n=0
                          l2.append(q)
                 
             elif y%i==0:
                        break

































        

    
    
