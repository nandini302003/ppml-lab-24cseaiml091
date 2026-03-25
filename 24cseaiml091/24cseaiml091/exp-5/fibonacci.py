list=[]
a,b=0,1
for i in range(10):
    list.append(a)
    a,b=b,a+b
print(list)
sum=0
for i in list:
    if(i%2==0):
        sum=sum+i
print("The sum of even valued terms are: ",sum)