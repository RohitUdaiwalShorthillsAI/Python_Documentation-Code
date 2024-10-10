s= set()
s.add(18)
s.add(18.0)
s.add('18')
print(len(s))  # 2 because numerically the 18 == 18.0 so one 18 is removed
print(s)