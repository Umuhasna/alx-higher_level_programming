#!/usr/bin/python3
'''Module'''


def inherits_from(obj, a_class):
    '''
    Checks whether the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: object
        a_class: class

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
