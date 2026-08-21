#!/usr/bin/env python3
"""Defines Fish, Bird, and FlyingFish classes to demonstrate
multiple inheritance and method resolution order (MRO).
"""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish, inheriting from both
    Fish and Bird (multiple inheritance).
    """

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")
