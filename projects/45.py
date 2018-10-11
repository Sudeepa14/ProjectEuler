def p(n):
    return(n*(n+1)/2)
def q(n):
    return(n*(3*n-1)/2)
def r(n):
    return(n*(2*n-1))
lp=[]
lq=[]
lr=[]
p=0
n=1
while n>p:
    p+=1
    n+=1
    lp.append(p(n))
    lq.append(q(n))
    lr.append(r(n))
    if i in lp==j in lq==k in lr:
        if i >40775:
            print(i)

    
