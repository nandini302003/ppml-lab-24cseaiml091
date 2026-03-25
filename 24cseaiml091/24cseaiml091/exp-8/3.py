str=input("Enter the paragraph: ")
wc=len(str.split())
print(f"No. of words are:{wc} ")
pc=0
for i in str.split():
    if(i==i[::-1]):
        pc+=1
print(f"The no. of palindrome exist are:{pc}")
print("Reverse words are: ")
for i in str.split():
   print(i[::-1])


    
    
