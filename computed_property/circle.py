from main import computed_property


class Circle:
    """
    A class to represent a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius=1):
        self.radius = radius

    @property
    @computed_property("radius")
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
