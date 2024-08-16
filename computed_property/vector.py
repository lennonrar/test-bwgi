from main import computed_property
from math import sqrt
class Vector:
    """
        A class to represent a vector with an optional color attribute.

        Attributes:
            x (int or float): The x-coordinate of the vector.
            y (int or float): The y-coordinate of the vector.
            z (int or float): The z-coordinate of the vector.
            color (str, optional): The color of the vector.
        """
    def __init__(self, x, y, z, color=None):
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    @computed_property('x', 'y', 'z', 90, 18, 6)
    def magnitude(self):
        """
                Computes the magnitude of the vector.

                Returns:
                    float: The magnitude of the vector.
                """
        print("computing magnitude")
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)