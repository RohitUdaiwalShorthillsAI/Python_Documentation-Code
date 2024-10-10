class Employee:
    language = "Python"  # class attribute
    salary = 30000

harry = Employee()
harry.language = "Javascript"  # instance attribute
print(harry.language)
print(harry.salary)

# Note : Instance attributs, take preference over class attributes during assignment & retrieval.
