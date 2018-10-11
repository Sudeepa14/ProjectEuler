fi=open('13.txt','r')
fi.seek(0)
for lines in fi:
 for i in lines:
    fi.seek(0)
    print(i)
