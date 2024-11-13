##python code for grade

n=int(input('enter marks'))
if (n>=35 and n<=40):
    print(n,"pass")

elif(n>=41 and n<=50):
    print(n,"D grade")


elif(n>=51 and n<=59):
    print(n,"c grade")


elif(n>=60 and n<=69):
    print(n,"b grade")


elif(n>=70 and n<=85):
    print(n,"A grade")

elif(n>=86 and n<=100):
    print(n,"A++ grade")

else:
    print(n,"fail")
    
                    
