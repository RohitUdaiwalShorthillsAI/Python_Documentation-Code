class Employee:
    company = "ITC"
    salary = 324202
    def show(self):
        print(f"The name is {self.company} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language : {self.language}")

class Programmer(Employee, Coder):
    company = "ITC infotech"

    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b= Programmer()

b.show()
b.printLanguage()
b.showLanguage()