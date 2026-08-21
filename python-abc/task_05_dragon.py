#!/usr/bin/env python3
"""Defines SwimMixin, FlyMixin, and a Dragon class that
combines them to demonstrate the mixin pattern.
"""


class SwimMixin:
    """Mixin providing swimming behavior."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying behavior."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon, composed of SwimMixin and FlyMixin
    to gain both swimming and flying abilities.
    """

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
