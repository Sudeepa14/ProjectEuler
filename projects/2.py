l=[]
s=0
p=0
while p<4000000 :
  x=1
  while True:
    n="%d"%(x)
    def f(n):
     if n==1:
         p=1
     if n==2:
         p=2
     elif int(n)>2:
         p=f(n-1)+f(n-2)
    l.append(p)
    x+=1
    if p>4000000 :
        break
for i in l:
    if i%2==0:
        s+=i
print(s)        
        
    

 
