p=3
s=1
for i in range(1,1000,2):
    s+=4*p+6*i+6
    p=p+4*i+6
    print(p)
print(s)
