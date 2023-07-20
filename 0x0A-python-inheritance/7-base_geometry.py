#!/usr/bin/python3
'''Module'''


class BaseGeometry:
    '''
    Modules:
        area:
        integer_validator:
    '''
    def area(self):
        '''
        Raise Exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        validates value

        Args:
            name:
            value:

        Returns:
            
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
