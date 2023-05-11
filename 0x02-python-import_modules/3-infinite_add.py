#!/usr/bin/python3

if __name__ == "__main__":
    """Print sum of arguments"""

    import sys
    args = sys.argv[1:]
    args_int = [int(arg) for arg in args]
    addition = sum(args_int)
    print(addition)
