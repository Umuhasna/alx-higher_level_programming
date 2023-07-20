#!/usr/bin/python3
"""
This is a module.

Classes:
    Square: that defines a square
"""


class Square:
    """
    Attributes:
        size (int): Private instance attribute

    Methods:
        area: returns the current square area

        my_print: prints in stdout the square with the character #
    """
    def __init__(self, size=0):
        """
        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size property.

        Returns:
            value of the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method that prints in stdout the square with the character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
