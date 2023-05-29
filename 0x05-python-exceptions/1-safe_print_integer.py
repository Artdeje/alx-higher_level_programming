#!/usr/bin/python3

#program that return true or false in exception
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
