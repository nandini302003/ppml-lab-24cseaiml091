a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
i=1
gcd=0
while(i<=a and i<=b and i<=c):
    if(a%i==0 and b%i==0 and c%i==0):
        gcd=1
    i+=1
print(f"The gcd of 3 number is: {gcd}")