from math import sqrt
from computed_property import computed_property

class Circle:
    """
    A class to represent a circle.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius=1):
        self.radius = radius

    @property
    @computed_property('radius')
    def diameter(self):
        """
        Computes the diameter of the circle.
        Returns:
        float: The diameter of the circle.
        """
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @diameter.deleter
    def diameter(self):
        self.radius = 0


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


def main():
    print(10*"-" + " Test Vector " + 10*"-")

    v = Vector(9, 2, 6)
    print(v.magnitude())
    v.color = 'red'
    print(v.magnitude())
    v.y = 18
    print(v.magnitude())
    help(v)

    print(10 * "-" + " Test Circle " + 10 * "-")
    circle = Circle()
    print(circle.diameter) # 2
    circle.diameter = 3
    print(circle.radius) # 1.5
    del circle.diameter
    print(circle.radius) # 0
    help(circle)


if __name__ == '__main__':
    main()