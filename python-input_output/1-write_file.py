#!/usr/bin/python3
"""Module for writing to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 file and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
