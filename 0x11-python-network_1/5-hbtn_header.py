#!/usr/bin/python3
'''
Docs
'''
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    html = get(url)
    print(html.headers.get('X-Request-Id'))
