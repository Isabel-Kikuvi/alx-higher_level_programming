#!/usr/bin/python3

if __name__ == "__main__":
    """Print number of args and list of args"""
    import sys

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for i in range(1, num_args+1):
        print(str(i) + ": " + sys.argv[i])
