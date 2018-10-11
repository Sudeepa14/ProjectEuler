p=0
s=0
for x in range(1,101):
    s+=x**2
    p+=x
q=(p)**2
print(q-s)
