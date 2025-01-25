# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Raises an error to indicate that the method should be implemented in a subclass."""
        raise NotImplementedError("The area method must be overridden by the subclass.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initializes a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initializes a Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)
