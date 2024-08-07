#__str__() function - returns from an init function.

class Perimeter:
    def __init__(self,length,width):
        self.length=length
        self.width = width


    def __str__(self):
        return f"{self.name}{self.width}"
    

sides = Perimeter(21,18)

print("The length is",sides.length)
print("The width is",sides.width)
    

