#wap to remove all theh duplicate from a given string 

x=int(input("enter a string "))
result=""
for char in x :
    if char not in result:
        result=result+char
print(result)        