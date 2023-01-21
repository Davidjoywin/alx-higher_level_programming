#!/usr/bin/python3
"""
Class Rectangle
"""
from base import Base


class Rectangle(Base):
    """
        Defining the rectange class
        Inherits from:
            Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            getting private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setting private attribute
        """
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """
            getting private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setting private attribute
        """
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """
            getting private attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setting private attribute
        """
        self.setter_validation('x', value)
        self.__x = value

    @property
    def y(self):
        """
            getting private attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setting private attribute
        """
        self.setter_validation('y', value)
        self.__y = value

    @staticmethod
    def setter_validation(attr, value):
        if not isinstance(value, int):
            raise TypeError(f"{attr} must be an integer")
        if (attr == "width" or attr == "height") and value <= 0:
            raise ValueError(f"{attr} must be > 0")
        if value < 0:
            raise ValueError(f"{attr} must be >= 0")

    def area(self):
        """
            Returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
            prints in stdout the rectangle instance with the character #
        """
        print('\n' * self.y)
        for height in range(self.height):
            for width in range(self.x + self.width):
                if width < self.x:
                    print(end=" ")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height
                                                                 )

    def update(self, *args, **kwargs):
        """
            update the attribute in a class
        """
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]

            except IndexError:
                pass

        else:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return None

    def to_dictionary(self):
        """
            Returns the dictionary representation of a rectangle
        """
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
