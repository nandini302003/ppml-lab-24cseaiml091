
s1 = float(input("Enter mark of Subject 1: "))
s2 = float(input("Enter mark of Subject 2: "))
s3 = float(input("Enter mark of Subject 3: "))
s4 = float(input("Enter mark of Subject 4: "))
s5 = float(input("Enter mark of Subject 5: "))


total = s1 + s2 + s3 + s4 + s5
percentage = (total / 250) * 100 

print("Total Marks:", total)
print("Percentage:", percentage)


if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")