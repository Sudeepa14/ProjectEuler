p=0
q=1
l1=[]
l2=[]
l3=[]
while q>p:
    p+=1
    q+=1
    l1.append(q*(q+1)/2)
    l2.append(q*(3*q-1)/2)
    l3.append(q*(2*q-1))
    for i in l3:
        for j in l2:
            if i==j:
                for k in l1:
                    if j==k and k!=40755.0 :
                        print(k) 
                        p=q
                        l3=[]
                        l2=[]
                        l1=[]
                   
