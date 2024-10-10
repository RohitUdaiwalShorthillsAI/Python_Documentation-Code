# The walrus operator (:=) - allows you to assing values to variables as part of an expression. This operator, named for its resemblance to the eyes and tasks of a walrus, is officially called "assignment expression"
# n = len([1,2,3,4,5])
if (n := len([1,2,3,4,5])) > 3 :
# if n>3:
    print(f"List is too long ({n} elements, expected <=3)")