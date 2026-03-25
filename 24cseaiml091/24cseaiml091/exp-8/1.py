l=[]
m=int(input("Enter m: "))
n=int(input("Enter n: "))
for i in range(m,n):
    l.append(i)
print("Elements in list are: ")
print(l)
sum=0
for i in l:
    sum=sum+i
print(f"The sum is:{sum}")
average=sum/len(l)
print(f"The average is:{average}")
largest=max(l)
print(f"The largest is:{largest}")
smallest=min(l)
print(f"The smallest is:{smallest}")
l1=[]
for i in l:
    if(i%3!=0):
        l1.append(i)
print(l1)