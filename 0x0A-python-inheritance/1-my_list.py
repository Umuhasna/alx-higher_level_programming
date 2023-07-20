#!/usr/bin/python3
'''This is module'''


class MyList(list):
    '''
    Class MyList that inherits from list
    '''
    def print_sorted(self):
        '''
        Public instance method that prints the list, but sorted (ascending sort)
        '''
        sorted_list = sorted(self)
        print(sorted_list)

