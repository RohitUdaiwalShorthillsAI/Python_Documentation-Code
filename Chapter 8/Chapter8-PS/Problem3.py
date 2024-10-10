# Recursive function to print first n natural number
def natural_print(n):
    if(n==1):
        print(1)
        return
    print(n)
    natural_print(n-1)

def sum_first_natural_number(n,sum):
    if(n==1):
        sum += n
        return sum
    sum += n
    return sum_first_natural_number(n-1,sum)

def sum_natural(n):
    if(n==1):
        return 1
    return n + sum_natural(n-1)

n = int(input("Enter a number : "))
# natural_print(n)
# print(f"The sum of first {n} natural number is {sum_first_natural_number(n,0)}")
print(f"The sum of first {n} natural number is {sum_natural(n)}")