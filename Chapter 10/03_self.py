# Self - it refers to the instance of the class. It is automatically passed with a function call from an object.
class Employee:
    language = "Python"  #This is a class attribute
    salary = 30000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod    # Sometimes we need a function that does not use the self-parameter. We can define a static method for this
    def greet():
        print("Good morning")

rohit = Employee()
rohit.getInfo() 
# Employee.getInfo(rohit)
rohit.greet()