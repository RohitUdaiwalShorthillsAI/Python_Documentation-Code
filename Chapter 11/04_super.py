class Employee:
    def __init__(self):
        print("Constructor is Employee")
    a = 1

class Coder(Employee):
    def __init__(self):
        print("Constructor is Coder")
    b=2

class Programmer(Coder):
    def __init__(self):
        super().__init__()
        print("Constructor is Programmer")
    c=3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # show an error as there is no b attribute in Employee class

o = Coder()
print(o.a,o.b)

o = Programmer()
print(o.a,o.b,o.c)