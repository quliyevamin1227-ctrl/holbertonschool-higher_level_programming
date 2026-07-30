#!/usr/bin/python3
def print_uppercase_twice(str=""):
    """Prints a string 2 times in uppercase followed by a new line."""
    str = str(str)
    result = ""

    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char

    print("{0}{0}".format(result))
