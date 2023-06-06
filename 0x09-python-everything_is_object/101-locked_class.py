#!/usr/bin/python3
# 101-locked_class.py

"""Defines the locked class."""


class LockedClass:
    """
    Prevent the user from instantiating the new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
