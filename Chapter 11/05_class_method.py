class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute a is {cls.a}")

e = Employee()
e.a = 34
e.show()