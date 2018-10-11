a=[75]
b=[95,64]
b1=[17,47,82]
c=[18 ,35, 87, 10]
d=[20 ,4, 82 ,47, 65]
e=[19 ,1, 23, 75 ,3 ,34]
f=[88 ,2, 77, 73, 7, 63, 67]
g=[99 ,65, 4, 28, 6, 16, 70, 92]
h=[41 ,41 ,26 ,56 ,83 ,40 ,80 ,70 ,33]
i=[41 ,48 ,72 ,33 ,47 ,32 ,37 ,16 ,94 ,29]
j=[53 ,71 ,44 ,65 ,25 ,43 ,91 ,52 ,97 ,51 ,14]
k=[70 ,11 ,33, 28, 77 ,73, 17, 78, 39, 68, 17, 57]
l=[91 ,71 ,52 ,38 ,17 ,14 ,91 ,43 ,58 ,50 ,27 ,29 ,48]
m=[63 ,66 ,4 ,68 ,89 ,53, 67, 30, 73, 16, 69, 87, 40, 31]
n=[4 ,62 ,98 ,27 ,23 ,9 ,70 ,98 ,73 ,93 ,38 ,53 ,60 ,4 ,23]
sum1=0
sss=0
for ii in a:
    iii=a.index(ii)
    for jj in [b[iii],b[iii+1]]:
       jjj=b.index(jj)
       for kk in [b1[jjj],b1[jjj+1]]:
        kkk=b1.index(kk)
        for ll in [c[kkk],c[kkk+1]]:
         lll=c.index(ll)
         for mm in [d[lll],d[lll+1]]:
           mmm=d.index(mm)
           for nn in [e[mmm],e[mmm+1]]:
              nnn=e.index(nn)
              for oo in [f[nnn],f[nnn+1]]:
                 ooo=f.index(oo)
                 for pp in [g[ooo],g[ooo+1]]:
                   ppp=g.index(pp)
                   for qq in [h[ppp],h[ppp+1]]:
                      qqq=h.index(qq)
                      for rr in [i[qqq],i[qqq+1]]:
                          rrr=i.index(rr)
                          for ss in [j[rrr],j[rrr+1]]:
                               sss=j.index(ss)
                               for tt in [l[sss],l[sss+1]]:
                                    ttt=l.index(tt)
                                    for uu in [m[ttt],m[ttt+1]]:
                                       uuu=m.index(uu)
                                       for vv in [n[uuu],n[uuu+1]]:
                                           vvv=n.index(vv)
                                           for ww in [n[vvv],n[vvv+1]]:
                                                sum1=ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+ss+tt+uu+vv+ww
                                                l1=[ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww]
                                                
                                                if sum1>sss:
                                                    sss=sum1
print(sss)
                                 
