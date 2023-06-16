#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_key = None
        max_value = list(a_dictionary.values())[0]
        for key, value in a_dictionary.items():
            if value > max_value:
                max_key = key
                max_value = value

        return max_key
