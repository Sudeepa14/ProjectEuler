li=[]
#def f5():
    #if y(1)==y(-1)and y(2)==y(-2):
        #list.append[p]
#def f6():
    #if y(1)==y(-1)and y(2)==y(-2) and y(3)==y(-3):
        #list.append[p]        
for x in range(100,1000):
    for i in range(100,1000):
        p=x*i
        q=str(p)
        y=list(q)
        l=0
        for n in y:
            l+=1
        if l==5:
            if y[0]==y[-1]and y[1]==y[-2]:
                 li.append(p)       
        elif l==6:
            if y[0]==y[-1]and y[1]==y[-2] and y[2]==y[-3]:
                 li.append(p)
print((max(li)))             
