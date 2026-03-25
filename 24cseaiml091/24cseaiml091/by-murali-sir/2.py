
class Addition:
    def add(self, a, b):
        return a + b


class Subtraction:
    def sub(self, a, b):
        return a - b

class Multiplication:
    def mul(self, a, b):
        return a * b

class Division:
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"



a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

add_obj = Addition()
sub_obj = Subtraction()
mul_obj = Multiplication()
div_obj = Division()


print("Addition:", add_obj.add(a, b))
print("Subtraction:", sub_obj.sub(a, b))
print("Multiplication:", mul_obj.mul(a, b))
print("Division:", div_obj.div(a, b))