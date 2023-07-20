#!/usr/bin/python3
"""
This is a module.

Classes:
    Rectangle: that defines a rectangle
"""


class Rectangle:
    """
    Attributes:
        width (int): Private instance attribute
        height (int): Private instance attribute

    Modules:
        area: returns the rectangle area
        perimeter: returns the rectangle perimeter
    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for the width property.

        Returns:
            value of the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height proprety
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns:
            int: the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns:
            int: the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        print the rectangle with the character #
        """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect

        for i in range(self.__height):
            rect += "#" * self.__width
            if i != self.__height - 1:
                rect += "\n"

        return rect

    def __repr__(self):
        """
        Returns:
            str: string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print the message Bye rectangle...
        """
        print("Bye rectangle...")
