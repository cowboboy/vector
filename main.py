class Coord:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        delattr(instance, self.name)


class Vector:
    x = Coord()
    y = Coord()
    z = Coord()

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z