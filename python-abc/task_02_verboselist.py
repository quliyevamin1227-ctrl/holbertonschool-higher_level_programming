#!/usr/bin/env python3
"""Defines a VerboseList class that extends list with notifications."""


class VerboseList(list):
    """A list subclass that prints a notification on every
    add/remove operation, while retaining normal list behavior.
    """

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print how many items were added."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Print a notification and remove the given item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification and pop the item at the given index."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
