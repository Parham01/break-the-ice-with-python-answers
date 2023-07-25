from math import pi

"""
Question 47:
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.
"""


class Radius:

    def __init__(self, r):
        self.r = r

    def compute_the_area(self):
        area = pi * self.r ** 2
        return area


circle1 = Radius(2)
print(circle1.compute_the_area())

"""
Question 48:
Define a class named Rectangle which 
can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_the_area(self):
        area = self.length * self.width
        return area


rectangle1 = Rectangle(4, 3)
print(rectangle1.compute_the_area())

"""
Question 49:
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape 
where Shape's area is 0 by default.
"""


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        area = self.length * self.length
        return area


sq1 = Square(2)

print(sq1.area())

"""
Question 50:
Please raise a RuntimeError exception.
"""

raise RuntimeError("ERROR!")
