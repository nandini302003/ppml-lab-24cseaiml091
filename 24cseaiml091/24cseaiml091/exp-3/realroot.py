import cmath
a=int(input('Enter 1st Coefficient: '))
b=int(input('Enter 2nd coefficient: '))
c=int(input('Enter  3rd coefficient: '))
delta=(b**2-4*a*c)
r1=(-b+cmath.sqrt(delta))/(2*a)
print(r1)
r2=(-b-cmath.sqrt(delta))/(2*a)
print(r2)