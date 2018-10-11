s=int(0)
y=1
x=2**1000
z=str(x)
while z[y-1]==z[-1]:
    s+=int(z[y-1])
    y+=1
print(s)    
