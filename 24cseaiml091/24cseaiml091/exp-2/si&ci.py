p=float(input('Enter p: '))
t=float(input('Enter t: '))
r=float(input('Enter r: '))
si=(p*t*r)/100
print('Simple Interst is: ',si)

##ci
amount=(p*(1+r/100)**t)
ci=amount-p
print("The Compound Interst is: ",ci)