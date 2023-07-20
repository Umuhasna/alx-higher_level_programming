#!/usr/bin/python3
'''This is module'''


def is_same_class(obj, a_class):
    '''
    Check whether the object is exactly an instance of the specified class

    Args:
        obj: object to check
        a_class: class

    Returns:
        True if the object is exactly an instance of the
        specified class; otherwise False
    '''
    return type(obj) is a_class
