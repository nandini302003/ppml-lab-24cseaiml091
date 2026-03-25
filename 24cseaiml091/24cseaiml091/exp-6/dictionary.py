n = int(input("Enter number of items: "))
my_dict = {}

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for {key}: ")
    my_dict[key] = value


values_dict = {}
for i, val in enumerate(my_dict.values(), start=1):
    values_dict[f"v{i}"] = val


print("\nOriginal Dictionary:")
print(my_dict)

print("\nValues Dictionary:")
print(values_dict)
