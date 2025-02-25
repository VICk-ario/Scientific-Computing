import math

#The function calculates and returns the area of the given shape.
def calculate_area(shape, dimension1, dimension2=None):
    if shape == "circle":
        return math.pi * (dimension1 ** 2)

    elif shape == "rectangle":
        if dimension2 is None:
            raise ValueError("Rectangle requires two dimensions.")
        return dimension1 * dimension2

    elif shape == "triangle":
        if dimension2 is None:
            raise ValueError("Triangle requires two dimensions.")
        return 0.5 * dimension1 * dimension2

    else:
        raise ValueError("Invalid shape. Please choose 'circle', 'rectangle', or 'triangle'.")

# Example usage
print(calculate_area("circle", 14))  # Should return the area of a circle
print(calculate_area("rectangle", 14, 21))  # Should return the area of a rectangle
print(calculate_area("triangle", 14, 21))  # Should return the area of a triangle