##for loop  using fibonacci

n= int(input('enter n='))
a=0
b=1
print(a,end="  ")
print(b,end="  ")
for i in range(n-1):
    c=a+b
    print(c,end="  ")
    a=b
    b=c
