def fu(n):
    li=[]
    n=0
    for i in range(2,n):
       y=i
       t=0
       l=0
       if y==2:
         return(k==1)
       for i in range(2,y):
            if y%i!=0:
              t+=1
              if t==y-2:
                 t=0
                 return(k==1)
                 
            elif y%i==0:
               return(k==0)
               break
       if k==1:
           for m in li:
               if not m==i:
                   p+=1
               if p==len(li):
                   n+=1
                   if n==4:
                       return('ok')
                   li.append(i)
               u=n/i
               fu(u)
p=0
q=1
r=2
s=3
while q>p:
    p+=1
    q+=1
    r+=1
    s+=1
    P=fu(p)
    Q=fu(q)
    R=fu(r)
    S=fu(s)
    if P==Q==R==S :
        print(P)
        break
            
    
