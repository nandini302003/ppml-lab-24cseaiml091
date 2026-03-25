digit = int(input("Enter a digit (0-6): "))

if digit == 0:
    print("Sunday")
elif digit == 1:
    print("Monday")
elif digit == 2:
    print("Tuesday")
elif digit == 3:
    print("Wednesday")
elif digit == 4:
    print("Thursday")
elif digit == 5:
    print("Friday")
elif digit == 6:
    print("Saturday")
else:
    print("Invalid input! Please enter a number between 0 and 6.")