import math

class Shape:
    def area(self):
        """
        Base class method that should be overridden by derived classes.
        Raises NotImplementedError to enforce method overriding.
        """
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Rectangle class constructor.
        
        Args:
            length (float): Length of the rectangle
            width (float): Width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Overrides the area method to calculate rectangle area.
        
        Returns:
            float: Area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Circle class constructor.
        
        Args:
            radius (float): Radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Overrides the area method to calculate circle area.
        
        Returns:
            float: Area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)
