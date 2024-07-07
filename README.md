Documentation:

Shape Class Hierarchy and Purpose:
The Shape class hierarchy is designed to represent various shapes such as circles, rectangles, and triangles. It provides a common interface for calculating the area and perimeter of different shapes, while also allowing for the inheritance of common attributes and behaviors.

Class Descriptions:
1.
Shape: The base class representing a generic shape. It has attributes for color and abstract methods for calculating the area and perimeter.
2.
Circle: A derived class representing a circle. It inherits from the Shape class and overrides the calculate_area() and calculate_perimeter() methods to calculate the area and perimeter of a circle.
3.
Rectangle: A derived class representing a rectangle. It inherits from the Shape class and overrides the calculate_area() and calculate_perimeter() methods to calculate the area and perimeter of a rectangle.
4.
Triangle: A derived class representing a triangle. It inherits from the Shape class and overrides the calculate_area() and calculate_perimeter() methods to calculate the area and perimeter of a triangle using Heron's formula.


Instructions to Run the Main Program:
1.
Save the provided code in a Python file (e.g., shape_hierarchy.py).
2.
Run the Python file using a Python interpreter or an IDE.
3.
The main program will create instances of different shapes (circle, rectangle, triangle) with specific dimensions and colors.
4.
It will use polymorphism to store the shape objects in a list or array.
5.
The program will iterate over the list of shapes and invoke the calculate_area() and calculate_perimeter() methods for each shape.
6.
The program will display the area, perimeter, and color of each shape.