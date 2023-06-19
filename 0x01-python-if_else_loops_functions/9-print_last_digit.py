#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print(f"{(-number) % 10:d}", end="")
        return (-number) % 10

    print(f"{number % 10:d}", end="")
    return number % 10
