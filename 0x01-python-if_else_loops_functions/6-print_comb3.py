#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if j > i and i != 8:
            print("{:d}{:d}, ".format(i, j), end="")
        elif i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
