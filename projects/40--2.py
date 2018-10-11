p=0
q=285
r=165
s=143
l1=[]
l2=[]
l3=[]
while q>r>s>p :
    p+=1
    q+=1
    r+=1
    s+=1
    l1.append(q*(q+1)/2)
    l2.append(r*(3*r-1)/2)
    l3.append(s*(2*s-1))
    for i in l3:
        for j in l2:
            if i==j:
                for k in l1:
                    if j==k and k!=40755.0 :
                        print(k) 
                        q=r
                        l3=[]
                        l2=[]
                        l1=[]
