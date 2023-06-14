#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [0] * len(my_list)
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]

    return new_list
