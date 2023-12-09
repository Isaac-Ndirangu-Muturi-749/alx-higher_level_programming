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

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
