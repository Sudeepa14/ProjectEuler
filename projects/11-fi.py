fi=open('11.txt','r')
a=0
q=fi.readlines()
p=fi.readline().split(' ')
a=0
l=[]
b=''
t=0
for p in q:
    for i in p:
        a=i
        if  i!=' ':
         print(i)
         
    
fi.close()
    
