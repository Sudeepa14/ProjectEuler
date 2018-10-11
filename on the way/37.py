def pri(s):
    s=int(s)
    global t
    n=0
    for i in range(2,s):
        if s%i==0:
            continue
        else:
            n+=1
            if n==s-2:
                t+=1


sum1=0
nn=0
p=3795
q=3796
while q>p:
    t=0
    p+=1
    q+=1
    
    for i in range(1,len(str(q))+1):
        tt=str(q)[(i-1):]
        pri(tt)
        if i!=1:
         ttt=str(q)[:-(i-1)]
         pri(ttt)
        
        if t==(len(str(q))*2)-1:
            nn+=1
            sum1+=(q)
            if nn==2:
                print(q,sum1,nn)
            if nn==11:
                p=q
                print(sum1)
        
        
