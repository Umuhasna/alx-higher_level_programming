#!/usr/bin/python3
'''
Docs
'''
from requests import post
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    html = post(url, data={'email': email}).text
    print(html)
