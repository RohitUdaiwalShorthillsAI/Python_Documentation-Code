friends = ["Orange", "Apple", "Rohan"]

print(friends)

#1. Append()
friends.append("Rohit")
print(friends)

#2. Sort()
friends.sort()
print(friends)

#3. reverse()
friends.reverse()
print(friends)

#4. insert()
friends.insert(3,"dDS")
print(friends)

#5. pop()
friends.pop(3)
print(friends)

#6. remove()
# friends.remove('Apple')
# print(friends)

#7. index()
print(friends.index('Apple'))

#8. extend()
friends.extend(['Rohit','Apple','Rohit'])
print(friends)

#9. count()
print(friends.count('Apple'))