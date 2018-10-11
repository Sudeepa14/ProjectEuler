x=13195
l=[]
p=[]
for n in range(2,x):
    s=n
    for i in range(1,s):
       if (n % i) == 0:
           p.append(i)
       else:
           l.append(i)
print(max(l))       
