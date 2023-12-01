#!/usr/bin/python3
'''
Docs
'''
from sys import argv
from requests import get


if __name__ == "__main__":
    url = argv[1]

    html = get(url)
    if html.status_code < 400:
        print(html.text)
    else:
        print('Error code: {}'.format(html.status_code))
