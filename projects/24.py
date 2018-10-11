
li=[1,2,3,4,5,6,7,8,9]
s=9
while s<1000001:

 for i in li:
    for j in li:
        s+=1

 for i in li:
    for j in li:
        for k in li:
            s+=1
 
 for i in li:
    for j in li:
        for k in li:
            for l in li:
             s+=1

 for i in li:
    for j in li:
        for k in li:
            for l in li:
             for m in li:
               s+=1

 for i in li:
    for j in li:
        for k in li:
            for l in li:
             for m in li:
              for n in li:
               s+=1
               if s==1000000:
                   print(str(i)+str(j)+str(k)+str(l)+str(m)+str(n))


 for i in li:
     for j in li:
        for k in li:
            for l in li:
                for m in li:
                 for n in li:
                  for o in li:
                   s+=1
                   if s==1000000:
                       print(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o))

