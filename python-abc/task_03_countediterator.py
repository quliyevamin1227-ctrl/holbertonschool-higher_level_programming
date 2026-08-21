#!/usr/bin/env python3
"""Defines a CountedIterator class that tracks how many items
have been fetched from an underlying iterator.
"""


class CountedIterator:
    """Wraps an iterable and counts how many items have been
    iterated over via __next__.
    """

    def __init__(self, iterable):
        """Initialize with the iterator of the given iterable
        and a counter set to 0.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Fetch the next item, increment the counter, and
        return it. Raises StopIteration when exhausted.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items fetched so far."""
        return self.count
