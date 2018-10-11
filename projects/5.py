s=[1,2]
p=[1,2]
for x in range(1,300000000):
 if x%20==x%19==x%18==x%17==x%16==x%15==0 :
     s.append(x)
for y in range (s[2],s[-1]):
 if y%14==y%13==y%12==y%11==0:
     p.append(y)
print(p[2])     
       
