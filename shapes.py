# Shape class
import math

class Shape:
    def __init__(self, color):
        self.color = color

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

# Circle class
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Rectangle class
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Triangle class
class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

# Main program
def main():
    shapes = [
        Circle("red", 2.5),
        Rectangle("blue", 4, 6),
        Triangle("green", 3, 4, 5)
    ]

    for shape in shapes:
        area = shape.calculate_area()
        perimeter = shape.calculate_perimeter()
        color = shape.get_color()

        print(f"Shape: {type(shape).__name__}")
        print(f"Color: {color}")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
        print("--------------------")

if __name__ == "__main__":
    main()