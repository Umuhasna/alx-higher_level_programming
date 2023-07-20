#!/usr/bin/python3
'''
This is a module

Classes:
    Square: defines a square
'''


class Square:
    '''
    Attributes:
        size (int): Private instance attribute

    Methods:
        area (int): returns the current square area
    '''
    def __init__(self, size=0):
        '''
        Args:
            size (int): size of the square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        Returns:
            int: the current square area
        '''

        return self.__size ** 2
