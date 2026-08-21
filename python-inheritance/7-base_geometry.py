#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Represents a base geometry object."""

    def area(self):
        """Raise an Exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): the name of the parameter.
            value (int): the value to validate.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
