#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for a built-in list class."""

    def print_sorted(self):
        """Print a list in an ascending order."""
        print(sorted(self))
