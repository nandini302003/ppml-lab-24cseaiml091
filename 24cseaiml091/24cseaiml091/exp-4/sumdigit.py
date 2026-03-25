n=int(input("Enter no. "))
sum=0
while(n!=0):
    rem=n%10
    sum=sum+rem
    n=n//10
print(f"The sum of digits is: {sum}")