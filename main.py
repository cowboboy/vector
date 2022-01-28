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

    def operation(func):
        """
        Decorator for plus and minus. It checks correct of values.
        """
        def wrapper(self, other):
            if not self.__check_value(other):
                raise ArithmeticError("Operands need to be type of Vector")

            return func(self, other)


        return wrapper

    @classmethod
    def __check_value(cls, value):
        """
        Output True if value is cls
        """
        return isinstance(value, cls)

    @operation
    def __add__(self, other):
        """
        Output sum of vectors
        """
        return self.__class__(*[sum(c) for c in zip(self.__coords, other.__coords)])

    @operation
    def __iadd__(self, other):
        return self + other

    @operation
    def __sub__(self, other):
        """
        Output sub of vectors
        """
        return self.__class__(*[c[0] - c[1] for c in zip(self.__coords, other.__coords)])

    @operation
    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        """
        If other is Vector output scalar mul of vectors
        If other is int output mul of vector and const
        """
        if isinstance(other, int):
            return self.__class__(*[other * c for c in self.__coords])
        return sum([c[0] * c[1] for c in zip(self.__coords, other.__coords)])

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other

    def __eq__(self, other):
        """
        Output True if double coords of Vectors are equal, False in another cases
        """
        return all([n[0] == n[1] for n in zip(self.__coords, other.__coords)])

    def __hash__(self):
        return hash(tuple(self.__coords))

    def __getitem__(self, item):
        return self.__coords[item]