#!/usr/bin/env python3
"""Defines an abstract Shape class, Circle/Rectangle subclasses,
and a shape_info function that relies on duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a shape."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        """Initialize a circle with the given radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with the given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of the given shape.

    Relies on duck typing: any object with area() and perimeter()
    methods can be passed, regardless of its actual class.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
