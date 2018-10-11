
#'1'=one=3
#'2'=two=3
#'3'=three=5
#'4'=four=4
#'5'=five=4
#'6'=six=3
#'7'=seven=5
#'8'=eight=5
#'9'=nine=4
#'10'=ten=3
#'11'=eleven=6
#'12'=twelve=6
#'13'=thirteen=8
#'14'=fourteen=8
#'15'=fifteen=7
#'16'=sixteen=7
#'17'=seventeen=9
#'18'=eighteen=8
#'19'=nineteen=8

def fu1(n):
    global p
    g=str(n)
    t=g[0]
    q=int(g[1])
    if q==0:
        if t=='2':
          p+=6
        elif t=='3':
          p+=6
        elif t=='4':
          p+=5
        elif t=='5':
          p+=5
        elif t=='6':
          p+=5
        elif t=='7':
          p+=7
        elif t=='8':
          p+=6
        elif t=='9':
         p+=6
    elif t=='2':
         p+=6
    elif t=='3':
        p+=6
    elif t=='4':
        p+=5
    elif t=='5':
         p+=5
    elif t=='6':
         p+=5
    elif t=='7':
         p+=7
    elif t=='8':
         p+=6
    elif t=='9':
         p+=6
    ################ second digit
    if q==1:  
           p+=3
    elif q==2:  
         p+=3   
    elif q==3:
         p+=5
    elif q==4:
         p+=4
    elif q==5:
         p+=4   
    elif q==6:
         p+=3
    elif q==7:
         p+=5
    elif q==8:
        p+=5
    elif q==9:
         p+=4

def fu2(n):
  global p
  e=str(n)
  y=int(e[0])
  if y==1:
      p+=13
      if e[1:]=='00':
          p-=3
      i=int(e[1:])
      if not i < 20:
       fu1(i)
  elif y==2:
      p+=13
      if e[1:]=='00':
          p-=3
      i=int(e[1:])
      if not i < 20:
       fu1(i)
  elif y==3:
      p+=15
      if e[1:]=='00':
          p-=3
      i=int(e[1:])
      if not i < 20:
       fu1(i)
  elif y==4:
      p+=14
      if e[1:]=='00':
          p-=3
      i=int(e[1:])
      if not i < 20:
       fu1(i)
  elif y==5:
      p+=14
      if e[1:]=='00':
          p-=3
      i=int(e[1:])
      if not i < 20:
       fu1(i)
  elif y==6:
      p+=13
      if e[1:]=='00':
          p-=3
      i=int(e[1:])
      if not i < 20:
       fu1(i)
  elif y==7:
      p+=15
      if e[1:]=='00':
          p-=3
      i=int(e[1:])
      if not i < 20:
       fu1(i)
  elif y==8:
      p+=15
      if e[1:]=='00':
          p-=3
      i=int(e[1:])
      if not i < 20:
       fu1(i)
  elif y==9:
      p+=14
      if e[1:]=='00':
          p-=3
      i=int(e[1:])
      if not i < 20:
       fu1(i)

p = int(106) # because
####################### 1-19#####################  
#########################################(  x01 - x019) -(x(1-9)
p+=106*9
p+=11
for l in range(20,100):
    fu1(l)
for o in range(100,1000):
    fu2(o)
print(p)
