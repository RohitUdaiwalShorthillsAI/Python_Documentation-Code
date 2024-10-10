#Class - class is a blueprint for creating object

class Employee:
    language = "Python"  #This is a class attribute
    salary = 30000

rohit = Employee()
rohit.name = "Rohit"
print(rohit.name)
print(rohit.language)
print(rohit.salary)

# Class attribute : An attribute that belongs to class rather than particular object
harry = Employee()
harry.name = "Harry"   # This is an instance attribut
print(harry.name)
print(harry.salary)

# Here name is object attribut and salary & laguage are class attributes as they are belongs to the class