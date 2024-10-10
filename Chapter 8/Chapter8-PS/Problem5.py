def rem(l,word):
    n =[]
    for item in l:
        n.append(item.strip('an'))
    return n

l = ["Harry","Rohit","Rohan","Manan", "Naman"]
print(rem(l,"Naman"))
