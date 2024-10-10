a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
try:
    print(f"The division of a/b is {a/b}")

except ZeroDivisionError as z:
    print(z)

