class Employee:
    def __init__(self, empid, name, basicpay):
       
        self.empid = empid
        self.name = name
        self.basicpay = basicpay
        
        self.da = 0.40 * self.basicpay
        self.ta = 0.10 * self.basicpay
        self.grosspay = 0 

    def calc(self):
       
        self.grosspay = self.basicpay + self.da + self.ta

    def disp(self):
        
        print("Employee ID:", self.empid)
        print("Name:", self.name)
        print("Basic Pay:", self.basicpay)
        print("DA (40% of Basic Pay):", self.da)
        print("TA (10% of Basic Pay):", self.ta)
        print("Gross Pay:", self.grosspay)


empid = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basicpay = float(input("Enter Basic Pay: "))

emp = Employee(empid, name, basicpay)


emp.calc()

emp.disp()
