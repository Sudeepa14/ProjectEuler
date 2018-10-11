

l=[2]
m=[]

def oddcon(x):
 z=x ################# z is the given number ##############################
 for j in range(l[-1],z):
  y=j
  n=0
  for i in range(2,y):
    if y%i!=0:
        n+=1
        if n==y-2:
         n=0
         l.append(j)
         t=y
                 
    elif y%i==0 and y%2!=0:
            m.append(j)
            break



        
