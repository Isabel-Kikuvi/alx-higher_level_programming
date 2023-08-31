#!/usr/bin/python3
"""a module that finds the peak i a list of ints"""


def find_peak(list_of_integers):
    """Function that returns peak of list of ints or none"""
    left = 0
    right = len(list_of_integers) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) \
                and (mid == len(list_of_integers) - 1
                     or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return None
