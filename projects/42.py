def fun(x):
    p=int(0)
    for i in x:
        if i=='A':
            p+=1
        elif i=='B':
            p+=2
        elif i=='C':
            p+=3
        elif i=='D':
            p+=4
        elif i=='E':
            p+=5
        elif i=='F':
            p+=6
        elif i=='G':
            p+=7
        elif i=='H':
            p+=8
        elif i=='I':
            p+=9
        elif i=='J':
            p+=10
        elif i=='K':
            p+=11
        elif i=='L':
            p+=12
        elif i=='M':
            p+=13
        elif i=='N':
            p+=14
        elif i=='O':
            p+=15
        elif i=='P':
            p+=16
        elif i=='Q':
            p+=17
        elif i=='R':
            p+=18
        elif i=='S':
            p+=19
        elif i=='T':
            p+=20
        elif i=='U':
            p+=21
        elif i=='V':
            p+=22
        elif i=='W':
            p+=23
        elif i=='X':
            p+=24
        elif i=='Y':
            p+=25
        elif i=='Z':
            p+=26
    y=[(1+8*int(p))**0.5-1]*2**(-1)
    if type(y)==int:
        q+=1
    p=0
f=open('word.txt','r')
y=f.readlines()
for i in y:
 z=i.split(',')
for r in z:
    t=r.strip('"')
    fun(t)
print(q)


