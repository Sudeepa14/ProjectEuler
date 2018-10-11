#c**2==a**2+b**2
#a+ b + c ==1000
#a < b < c
#type(a)==int
#type(b)==int
#type(c)==int
#a<1000/3
for a in range(1,334):
    for b in range(250,1000):
      if 1000**2-2000*(a+b)+2*a*b==0 :
          print(a*b*(1000-(a+b)))
         
      
