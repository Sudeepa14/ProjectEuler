n=0
p=0
for r in range(2,10,2):
      for i in range(1,10,r):
         n+=i
         p+=1
         if p==4:
              p=0
              break
print(n)         
