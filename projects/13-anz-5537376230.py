fi=open('13-2.txt','r')
s=0
for x in fi:
        if x!='' :
            s+=int(x)
s=str(s)
print(s[:10])
