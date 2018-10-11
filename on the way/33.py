s=1
ss=1
for i in range(10,100):
    for j in range(10,100):
        k=i/j
        if k<1 and i%10!=0 and j%10!=0 and str(i)[0]!=str(i)[1] and str(j)[0]!=str(j)[1]   :
           if str(i)[1]==str(j)[0] or str(i)[0]==str(j)[1]: 
              if k==int(str(i)[0])/int(str(j)[1]):
                s*=int(str(i)[0])
                ss*=int(str(j)[1])
                print(i,j)
          
for t in range(1,s):
    if ss%t==0 and s%t==0:
        ss=ss/t
print(ss)
