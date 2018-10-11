ll=0 
for jj in range(1,366):
    if jj%7==0:
        l=jj
        if l>ll:
            ll=l
        
print(ll)
x=7-(365-ll)
j=0 #for 2000
for i in range(1901,2001):    
    if int(str(i)[-2:])%4==0:
        j+=366
    else:
        j+=365
n=0
for k in range(x,(j-4),7):
    n+=1
    
    print(k)
print(n)


def p(n):
    if p<31:
        k=31-j

    ifp<
