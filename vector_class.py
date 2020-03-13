
# This is python program to make vector class with  special method.
class vector:
    def __init__(self,d):      # here d is define for number of dimension.
        self.coords = [0] * d
    
    def show_vector(self):
        print(self.coords)
    
    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self,j):
        return self.coords[j]
    
    def __setitem__(self,j,value):
        self.coords[j] = value
    
    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError("dimensions must same.")
        else:
            result = vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] + other[j]
            return result
    
    def __eq__(self,other):
        return self.coords == other.coords
    
    def __ne__(self,other):
        return not self.coords == other.coords
    
    def __str__(self):
        return f"< {str(self.coords)[1:-1]} >"


v1 = vector(3)
print("v1:",v1)
print("length:",len(v1))
for n in range(3):
    v1[n] = n
print("v1:",v1)

v2 = vector(3)
v2[0] = 45
v2[1] = 10
print("v2:",v2)
v3 = v1+v2
print("v3:",v3)

print(type(v1))

print(v1 == v2)

print(v1 != v2)