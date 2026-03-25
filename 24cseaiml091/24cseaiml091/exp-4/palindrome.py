n=int(input("Enter the number: "))
rev=0
org=n
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(org==rev):
    print("Palindrome") 
else:
    print("Not Plaindrome")
    