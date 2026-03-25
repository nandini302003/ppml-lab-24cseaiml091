'''p=100
r=10
t=5

si=p*t*r/100
print("the simple interst is =",si)

ci = p * ((1 + r/100) ** t) - p
print("the compound intrest is =",ci)'''



p=float(input("enter principal value="))
t=float(input("enter time value="))
r=float(input("enter rate value="))
si=p*t*r/100
print("the simple interst is =",si)
ci = p * ((1 + r/100) ** t) - p
print("the compound intrest is =",ci)