s=0
fl=open('11.txt','r')
for line in fl:
    for ch in line:
        s+=int(ch)
print(s)
fl.close()

