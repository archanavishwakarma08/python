##nested if (if within if)
##if(cond1):
##    if(cond2):
##        ......
##        ......
##        
##    else:
##        ......
##        ......
##
##
##else:
##    if(cond 3):
##        ......
##        ......
##    else:
##        .....
##        ......
##        
#prog for largest of 3 no with using nested if

a=int(input("enter the no="))
b=int(input("enter the no="))
c=int(input("enter the no="))

if(a==b and b==c):
    print('no are the same')

else:
    if(a>b):
        if(a>c):
            print(a,"is greater than",b,c)

        else:
            print(c,"is greater than",a,b)
            
    else:
        if(b>c):
            print(b,"is greater than",a,c)
            
        else:
             print(c,"is greater than ",a,b)
            
      



        


        
    
    
















    


        
