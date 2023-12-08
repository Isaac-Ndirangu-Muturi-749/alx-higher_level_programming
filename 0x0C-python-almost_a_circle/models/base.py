#!/usr/bin/python3
"""Defines the Base class."""


class Base:
    """Base class for managing id attribute in other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of Base.

        Args:
            id (int): If provided, assigns the value to the public
                instance attribute id. Otherwise, increments __nb_objects
                and assigns the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
