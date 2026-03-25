#factorial of a number 
n=int(input("enter a number for factorial:"))
if(n<0):
    print("enter a positive number:")
elif(n==0):
    print("the factorial of 0 is :",0)
else:
    fact=1
    for i in range (1,n+1):
        fact = fact*i
    print(f"the factrial of {n}is :{fact}")
