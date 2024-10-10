s1 = {2,1,12,12}
s2 = {24,325,32,21,2,1}
print(s1.union(s2))
print(s1.intersection(s2))
#1. Difference set
print(s1 - s2)
#2. Difference_Update
# s1.difference_update(s2)
# print(s1)
#3. isdisjoint()  - Returns True if two sets have a null intersection
print(s1.isdisjoint(s2))
#4. issubset()  - Returns True if another set contains this set
print(s1.issubset(s2))
#5. issuperset() - Returns True if this set contains another set
print(s2.issuperset(s1))
#6. symmetric_difference()/Update() - Returns a set with elements in either the set or other but not both
print(s1.symmetric_difference(s2))

