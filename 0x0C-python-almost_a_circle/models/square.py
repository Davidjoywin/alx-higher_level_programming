#!/usr/bin/python3
"""
class Square
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
        square class that inherit from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            getting attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            setting attribute
        """
        self.setter_validation("width", value)
        self.width = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width
                                                         )

    def update(self, *args, **kwargs):
        """
            update the class square
        """
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "size"),
                'y': getattr(self, "y")}
