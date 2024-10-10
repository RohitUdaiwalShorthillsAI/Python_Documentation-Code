class Employee:
    language = "Python"  #This is a class attribute
    salary = 30000

    def __init__(self, name, salary, language):   # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


rohit = Employee("Rohit", 35000, "Javascript")
# harry.name = "Harry"
print(rohit.name, rohit.salary)
