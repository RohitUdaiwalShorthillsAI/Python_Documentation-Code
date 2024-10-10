try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("Python_Documentation-Code/Chapter 12/Chapter12-PS/2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("/home/shtlp_0108/Desktop/Python_Practice/Python_Documentation-Code/Chapter 12/Chapter12-PS/3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank YOU")