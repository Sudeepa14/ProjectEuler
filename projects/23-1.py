li=[]
def abd(n):
    p=0
    q=0
    for t in range(1,n):
        if n%t==0:
            p+=t
    if p==t:
        li.append(n)




for i in range(1,28123):
    for j in range(1,i):
        abd(j)
        if not q==1:
            abd(
    
