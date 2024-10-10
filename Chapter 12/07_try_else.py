try:
    a = int(input("Hey, Enter a number : "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")

# Sometimes we want to run a place of code when try was successful.
