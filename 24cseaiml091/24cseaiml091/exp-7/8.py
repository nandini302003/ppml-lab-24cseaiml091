def largest(a,b,c):
    if(a>b and a>c):
        return (f"{a} is greatest")
    elif(b>a and b>c):
        return (f"{b} is greatest")
    elif(c>a and c>b):
        return (f"{c} is greatest")
    else:
        return "Invalid"
a=int(input("Enter: "))
b=int(input("Enter: "))
c=int(input("Enter: "))                                                            
print(largest(a,b,c))