# Definition - Set is a collection of non-repetitive elements.
d = {}  # Empty Dictionary
print(type(d))  # type is dictionary
f = []
print(type(f))  # type is list
g = ()
print(type(g))  # type is tuple
s = set() # Don't usd s = {} as it will create an empty dictionary
print(type(s))  # type is set

s = {21,1,1,224,24,23,32,2,41,132,21,211,321,134,22,2, "Rohit"}
s.add(342)
print(s)

# Properties
# 1. Sets are unordered => Element's order doesn't matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change item in sets.
# 4. Set cannot contain duplicate values.