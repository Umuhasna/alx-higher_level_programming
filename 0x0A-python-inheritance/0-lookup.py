#!/usr/bin/python3
'''This is a module'''


def lookup(obj):
    '''
    Functions to look up for all attributes and methods of an object

    Args:
        obj: object to look into

    Returns:
        list of available attributes and methods of an obj
    '''
    return dir(obj)
