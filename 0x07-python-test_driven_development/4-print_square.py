#!/usr/bin/python3
"""Defines the square-printing a function."""


def print_square(size):
    """Print the square with # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not the integer.
        ValueError: If size is < 0
    """
if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
