#!/usr/bin/python3
"""Defines a matrix div funcction"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix

    Args:
        matrix: list of int or float
        div: divisor

    Raises:
        Typerror: if matrix is not list of list
        Typeerror: if matrix is not regular
        Typeerror: if matrix contain anthing other than int & float
        Typeerror: if div is not a number
        ZeroDivisionError: if div is 0

    Returns:
        the new list without mutating the original list
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(i)
        elif size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for n in i:
            if type(n) is not int and type(n) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in i] for i in matrix]
