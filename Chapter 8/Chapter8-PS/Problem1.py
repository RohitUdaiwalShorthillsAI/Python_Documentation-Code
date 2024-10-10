def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else: 
        return c


a = int(input("Enter your number 1 : "))
b = int(input("Enter your number 2 : "))
c = int(input("Enter your number 3 : "))

print(greatest(a,b,c))