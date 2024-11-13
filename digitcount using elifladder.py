#print the how many digit of a given no

n=int(input("enter the number="))
if(n>0 and n<9):
    print("Single digit number")

elif(n>=10 and n<=99):
    print("two digit no")

elif(n>=100 and n<=999):
    print("three digit no")

    
else:
    print("more than three digit")
