import math

class Vector:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, *coords):
        self.__coords = coords

    def __str__(self):
        return f"Вектор с координатами {self.__coords}"

    def __abs__(self):
        """
        Output length of Vector
        """
        return round(math.sqrt(sum(map(lambda x: x ** 2, self.__coords))), 2)

    def __len__(self):
        """
        Output dimension of the vector
        """
        return len(self.__coords)

    def __add__(self, other):
        """
        Output sum of vectors
        """
        return self.__class__(*[sum(c) for c in zip(self.__coords, other.__coords)])

