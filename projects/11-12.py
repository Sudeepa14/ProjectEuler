fi=open('11.txt,'r')
p=1
for i in range(1,21):
        x=fi.readline(i)
        y=x[-1:]
        q*=int(y[i-1])
        p*=int(x[i-1])

fi.close()
        
