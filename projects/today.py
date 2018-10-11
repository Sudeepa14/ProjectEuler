fi=open('11.txt','r')
a=0
p=fi.read().split(' 'or '\n' )
v=8
w=1
x=1
y=1
z=1
for i in range(0,19):
    v*=int(p[i])
for j in range(0,381,21):
    if  len(p[j])<3:
        w*=int(p[j])
    else:
        w*int((str(p[j]))[0:2])
for k in range(0,370,20):
    if k==0:
        y*=8
    else:
        
      x*=int(p[k][-1:])
for l in range(360,380):
    if  len(p[l])<3:
        z*=int(p[l])
    else:
        z*=int(p[l][:2])
        
li=[v,w,x,y,z]

    
print(max(li))
