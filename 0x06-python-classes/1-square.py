#!/usr/bin/python3
'''
This is a class Square.

Classes:
    Square: class that defines a square
'''


class Square:
    '''
    Attributes:
        size (int): the size of the square
        Private instance attribute: size
    '''

    def __init__(self, size):
        '''
        Args:
            size (int): size of the square
            Instantiation with size (no type/value verification)
        '''
        self.__size = size
