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
        position (int): Private instance attribute

    Methods:
        area: returns the current square area

        my_print: prints in stdout the square with the character #
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): size of the square
            position (int): position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter method for the position proprety
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not
                all(isinstance(i, int)for i in value) or
                all(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
