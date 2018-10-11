y=int(input('enter the number:'))
n=0
l=0
if y==2:
 print(y,"is  a prime number")
else:
 for i in range(2,y):
       if y%i!=0:
              n+=1
              if n==y-2:
                 n=0
                 print(y,"is  a prime number")
                 
       elif y%i==0:
               print(y,"is not a prime number")
               break





