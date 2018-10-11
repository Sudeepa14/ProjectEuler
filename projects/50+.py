s=0
x=[2,3]
m=[]
p=1
t=0
q=3
while q>p:
    y=q
    n=0
    l=0
    for i in range(2,y):
       if y%i!=0:
              n+=1
              if n==y-2:
                 n=0
                 x.append(y)
                 o=x[:-1]
                 for i in o :
                  s+=i
                  if s==q:
                     if  s<10:
                         t=q
                
                     else:
                       print(t)
                       p=1
                       q=1


