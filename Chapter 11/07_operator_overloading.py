class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    
    def __sub__(self,num):
        return self.n - num.n
    
    def __mul__(self,num):
        return self.n*num.n
    
    def __truediv__(self,num):
        return self.n/num.n
    
    def __floordiv__(self,num):
        return self.n//num.n

n = Number(3)
m = Number(4)

print(m+n)
print(m-n)
print(m*n)
print(m/n)
print(m//n)

# str__() - used to set what gets displayed upon calling str(obj)

# __len__() - used to set what gets displayed upon calling len(obj)
