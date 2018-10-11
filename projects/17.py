
####################### 1-19#####################
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

######################### 20-99#######################
######l(0)
#'2'=twenty=6
#'3'=thirty=6
#'4'=forty=5
#'5'=fifty=5
#'6'=sixty=5
#'7'=seventy=7
#'8'=eighty=6
#'9'=ninety=6
######l(1)
#'1'=one=3
#'2'=two=3
#'3'=three=5
#'4'=four=4
#'5'=five=4
#'6'=six=3
#'7'=seven=5
#'8'=eight=5
#'9'=nine=4
p=int(106)
for i in range(20,99):
    n=str(i)
    s=list(n)
    q=int(s[1])
    if s[0]=='2':
      p+=6   
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
    elif s[0]=='3':
      p+=6
      if q==1:  # or int( q)
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
    elif s[0]=='4':
      p+=5
      if q==1:  # or int( q)
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
    elif s[0]=='5':
      p+=5
      if q==1:  # or int( q)
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
    elif s[0]=='6':
      p+=5
      if q==1:  # or int( q)
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
    elif s[0]=='7':
      p+=7
      if q==1:  # or int( q)
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
    elif s[0]=='8':
      p+=6
      if q==1:  # or int( q)
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
    elif s[0]=='9':
      p+=6
      if q==1:  # or int( q)
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

for i in range(100,999):
    m=str(i)
    z=list(m)
    a=int(z[0])
    if a==1:
        p+=13
    elif a==2:
        p+=13    
    elif a==3:
        p+=15
    elif a==4:
        p+=14
    elif a==5:
        p+=14  
    elif a==6:
        p+=13
    elif a==7:
        p+=15
    elif a==8:
        p+=15
    elif a==9:
        p+=14
     # second to 3 byte
    b=int(z[1])
    if b==2:
        p+=6
    elif b==3:
        p+=6
    elif b==4:
        p+=5
    elif b==5:
        p+=5   
    elif b==6:
        p+=5
    elif b==7:
        p+=7
    elif b==8:
        p+=6
    elif b==9:
        p+=6
    c=z[2]   
    if c=='1':  # or int( q)
        p+=3
    elif c=='2':  
        p+=3   
    elif c=='3':
        p+=5
    elif c=='4':
        p+=4
    elif c=='5':
        p+=4   
    elif c=='6':
        p+=3
    elif c=='7':
        p+=5
    elif c=='8':
        p+=5
    elif c=='9':
        p+=4 
print(p)   
#############################100-999
#'1'=one hundred and=13
#'2'=two hundred and =13
#'3'=three hundred and=15
#'4'=four hundred and=14
#'5'=five hundred and =14
#'6'=six hundred and =13
#'7'=seven hundred and=15
#'8'=eight hundred and=15
#'9'=nine hundred and =14


        
