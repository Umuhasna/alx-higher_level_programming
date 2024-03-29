#!/usr/bin/python3
'''This is module'''


def is_kind_of_class(obj, a_class):
    '''
    checks whether the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj: object to check
        a_class: class

    Returns:
        True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class;
        otherwise False
    '''
    if isinstance(obj, a_class):
        return True

    return False
