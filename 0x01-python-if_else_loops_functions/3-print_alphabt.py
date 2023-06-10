#!/usr/bin/python3
for letters in range(97, 123):
    if letters == 101 or letters == 112:
        continue
    print("{:c}".format(letters), end="")
