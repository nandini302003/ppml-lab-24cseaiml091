m = int(input("Enter m: "))
n = int(input("Enter n: "))

count = 0

for i in range(m, n):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:  
            print(i)
            count += 1

print("Count:", count)
