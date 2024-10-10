'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1

factorinal(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n = int(input("Enter your number : "))
print(f"The factorial of {n} is {factorial(n)}")