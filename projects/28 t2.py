n=1
p=0
for r in range(2,1001,2):
      for i in range(3,1002001,r):
         n+=i
         p+=1
         if p==4:
              break
              p=0
print(n)         
