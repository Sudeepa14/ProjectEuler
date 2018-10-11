a={'i':200,'j':100,'k':50,'l':20,'m':10,'n':5,'o':2,'p':1}
n=0
for b in range(0,1):
    
    for c in range(0,2):
       
        for d in range(0,5):

            for e in range(0,11):

                for f in range(0,21):

                    for g in range(0,41):

                        for h in range(0,101):

                            for z in range(0,201):

                                if b*a.get('i')+c*a.get('j')+d*a.get('k')+e*a.get('l')+f*a.get('m')+g*a.get('n')+h*a.get('o')+z*a.get('p')==200:
                                    n+=1
print(n)
