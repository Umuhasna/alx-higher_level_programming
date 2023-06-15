#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        new_uniq_list = []
        result = 0
        for i in range(len(my_list)):
            if my_list[i] not in new_uniq_list:
                new_uniq_list.append(my_list[i])

        for i in range(len(new_uniq_list)):
            result += new_uniq_list[i]

        return result
