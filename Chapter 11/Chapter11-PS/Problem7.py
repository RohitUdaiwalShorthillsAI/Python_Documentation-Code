class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x*other.x + self.y*other.y + self.z*other.z
        return result

    def __str__(self):
        result = f"{self.x}i + {self.y}j + {self.z}k"
        return result
    
    def __len__(self):
        return 3


v1 = Vector(1,2,3)
print(len(v1))
