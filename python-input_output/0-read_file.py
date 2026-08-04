#!/usr/bin/python3
"""Module for reading a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
