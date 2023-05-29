#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    var_int = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: ", e, file=sys.stderr)
        var_int = False
    return var_int
