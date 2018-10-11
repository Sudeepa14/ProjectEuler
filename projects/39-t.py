
f=open('word.txt','r')
x=f.read()
for i in x:
    if i=='"':
        print(f.read(i+1:,'"'))
f.close()
