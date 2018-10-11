def z(n):
 if n==1:
     return(1)
 else:
    return(z(n-1)+ n**n )
x=z(994)
for i in range(995,1001):
    x+= i**i
y=str(x)
print(y[-10:])


    ##this definition doesn't give the value of z(1000) so u have to use another way like i used

    
