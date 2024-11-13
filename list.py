list=[10,22,45,67,'java',]
print(list)
print(list[2])


#add elemnts
list.append('python')
print(list)

#insert the value into list
list.insert(3,'here is an exaxmple')
print(list)


##update the elements
list[4]='vb.net'
print(list)
      

#pop the elements
list.pop()
print(list)

#remove the single elements
print(list)
no=input('enter the value=')
if no in list:
    list.remove(no)
else:
    print('element is not there')
print(list)

    
