#!/usr/bin/python3
"""Defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle's position.
            y (int): y-coordinate of the rectangle's position.
            id (int): ID of the rectangle. If None, it will be assigned by
                the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_integer(self, name, value):
        """Validate if the given value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def validate_positive(self, name, value):
        """Validate if the given value is greater than 0."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_non_negative(self, name, value):
        """Validate if the given value is greater than or equal to 0."""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
