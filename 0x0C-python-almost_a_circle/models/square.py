#!/usr/bin/python3
"""Defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of Square.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square's position.
            y (int): y-coordinate of the square's position.
            id (int): ID of the square. If None, it will be assigned by
                the Base class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the Square."""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, val in enumerate(args):
                setattr(self, attrs[i], val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
