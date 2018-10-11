l=[]
m=[]
k=0
j=[]
x=600851475143
for y in range(1,x/2):
    if x/y==0:
        l.append(y)
        k=k+1
for p in range(0,k):
    for n in range(2,l(p)):
        if l(p)%n==0:
            m.append(l(p))
j=[l-m]
print(j(-1))
