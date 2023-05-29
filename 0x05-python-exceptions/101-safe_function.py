#!/usr/bin/python3

from __future__ import print_function
import sys

""" This function will execute the safety of code's function"""

def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
