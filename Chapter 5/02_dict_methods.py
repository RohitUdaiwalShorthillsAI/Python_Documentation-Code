marks = {
    "Harry" : 100,
    "Rohit" : 89,
    "Shubhan" : 23,
    "list" : [23,34,12]
}

print(len(marks))

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"Harry":99, "Rohan":45})
# print(marks)

# print(marks.get("Harry2"))  # prints None
# print(marks["Harry2"])  # return error

# 1. clear()
# print(marks.clear())   # return None

# print(marks)

# 2. copy()
# new_marks = marks.copy()
# print(new_marks)

# 3. get()
# print(marks.get("Rohit"))  # Returns the value for the specified key
# print(marks.get("Vishnu",23)) # if key is in the dictionary then provide value otherwise print default value

# 4. pop()
# marks.pop("Harr", 43)

# setdefault()
marks.setdefault("Vishnu", 44)
print(marks)