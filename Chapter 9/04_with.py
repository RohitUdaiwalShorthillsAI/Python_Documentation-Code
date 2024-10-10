f = open("Chapter 9/file.txt")

print(f.read())
f.close()

# The same can be written using 'with' statement like this :
with open("Chapter 9/file.txt") as f:
    print(f.read())

# You don't have to explicitly close the file
