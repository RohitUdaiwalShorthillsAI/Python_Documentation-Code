def F_to_C(f):
    return 5*(f-32)/9
f = int(input("Enter temperature in F : "))
c = F_to_C(f)
print(f"{round(c)} celsius")