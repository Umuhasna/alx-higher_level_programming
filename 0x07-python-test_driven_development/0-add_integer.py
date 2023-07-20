#!/usr/bin/python3
""" Addition module """


def add_integer(a, b=98):
    """
    Add two integers and return their sum

    Args:
        a: a float or integer type
        b: a float or int type

    Raises:
        TypeError: if the argument are not int or float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
