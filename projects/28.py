n=0
for r in range(2,1000,2):
      p=0
      for i in range(1,1002002,r):
         n+=i
         p+=1
         if p==4:
              break
print(n)         
