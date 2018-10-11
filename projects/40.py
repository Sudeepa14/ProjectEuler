s=''
for i in range(1,1000001):
    s=s+str(i)
def d(n):
    y=float(s[n])*10**(-1*n)
    return(y)
y=1
p=1
for n in range(1,8):
    p=p*10**(n-1)
    y=y*d(p)
print(y)
 
