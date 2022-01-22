import math
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
class Triangle(Shape):
    def area(self):
        return self.width * self.height / 2

class Rectangle(Shape):
    def area(self):
        return self.width * self.height


trngl = Triangle(7, 10)
rctgl = Rectangle(7, 10)

print(trngl.area(), rctgl.area())