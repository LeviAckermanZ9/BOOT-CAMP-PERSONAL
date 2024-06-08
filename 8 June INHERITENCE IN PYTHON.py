# Single Inheritance
class Shape:
    def __init__(self, color):
        self.color = color

    def display_info(self):
        return f"Color: {self.color}"

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def display_info(self):
        return f"Triangle - {super().display_info()}, Base: {self.base}, Height: {self.height}"

# Multiple Inheritance
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        return f"Sides: {self.sides}"

class Pentagon(Shape, Polygon):
    def __init__(self, color, sides, length):
        Shape.__init__(self, color)
        Polygon.__init__(self, sides)
        self.length = length

    def display_info(self):
        return f"Pentagon - {super().display_info()}, {super(Pentagon, self).display_info()}, Length: {self.length}"

# Method Overriding
class Hexagon(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def display_info(self):
        return f"Hexagon - {super().display_info()}, Side Length: {self.side_length}"

# Instantiating objects
my_triangle = Triangle("Yellow", 5, 8)
my_pentagon = Pentagon("Purple", 5, 10)
my_hexagon = Hexagon("Orange", 6)

# Using methods
print(my_triangle.display_info())   # Output: Triangle - Color: Yellow, Base: 5, Height: 8
print(my_pentagon.display_info())   # Output: Pentagon - Color: Purple, Sides: 5, Length: 10
print(my_hexagon.display_info())    # Output: Hexagon - Color: Orange, Side Length: 6
