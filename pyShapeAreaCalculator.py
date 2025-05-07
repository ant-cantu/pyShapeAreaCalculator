import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (float(self.radius) * float(self.radius))

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return float(self.length) * float(self.width)
        

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * float(self.base) * float(self.height)
        

#*********************************************************

print("*** Basic Shape Calculator ***")

while True:
    try:
        print("\nSelect which shape you would like to find the area:")
        print("   1. Calculate Area of Cirlce")
        print("   2. Calculate Area of Rectangle")
        print("   3. Calculate Area of Triangle")
        print("   4. Exit Application")

        selection_str = input("Selection: ")
        selection = int(selection_str)

        if selection == 1:
            radius = float(input("\nInput the radius of the circle: "))
            if radius > 0:
                circle = Circle(radius)
                print(f"\nThe area of the circle is: {circle.calculate_area():.2f}")
            else:
                print("Error: The radius must be a positive number.")
        elif selection == 2:
            length = float(input("\nInput the length of the rectangle: "))
            width = float(input("Input the width of the rectangle: "))
            if length > 0 and width > 0:
                rectangle = Rectangle(length, width)
                print(f"\nThe area of the rectangle is: {rectangle.calculate_area():.2f}")
            else:
                print("Error: The length and width must be a positive number.")
        elif selection == 3:
            base = float(input("\nInput the base of the triangle: "))
            height = float(input("Input the height of the triangle: "))
            if base > 0 and height > 0:
                triangle = Triangle(base, height)
                print(f"\nThe area of the triangle is: {triangle.calculate_area():.2f}")
            else:
                print("Error: The base and height must be a positive number.")
        elif selection == 4:
            print("\nExiting applicaiton")
            break
        else:
            print("\nError: Invalid input")
    except ValueError:
        print("\nError: Invalid input")

    