a=float(input('Enter a: '))
b=float(input('Enter b: '))
c=float(input('Enter c: '))
perimeter = a+b+c
s= perimeter /2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('Perimeter of triangle is: ',perimeter)
print('Semi-Perimeter is: ',s)
print('Area is: ',area)