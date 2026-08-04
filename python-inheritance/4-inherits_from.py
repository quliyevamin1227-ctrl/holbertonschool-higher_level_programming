#!/usr/bin/python3
"""Module for inherits_from"""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class, otherwise False"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
