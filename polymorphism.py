# class square
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print("my area is:", self.side**2)

# class circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("my area is:", 3.14 * self.radius*self.radius)

# object creation
osquare = Square(5)
ocircle = Circle(5)

# iterating through the objects
for shape in (osquare, ocircle):
    shape.area()  