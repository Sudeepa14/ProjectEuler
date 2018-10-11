
fh= open( "11.txt", "r" )
a= []
b=0
for line in fh:
    a.append( line.strip())
    print(a)
for t in a:
        b+=int(t)
        
print(b)        
fh.close()
