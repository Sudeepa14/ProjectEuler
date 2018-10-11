p=1
q=2
while q>p:
    p+=1
    q+=1
    if q%11==0 and q%12==0 and q%13==0 and q%14==0 and q%15==0 and q%16==0 and q%17==0 and q%18==0 and q%19==0 and q%20==0:
      print(q)
      p=q
      break
