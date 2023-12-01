#!/usr/bin/python3
'''
Docs
'''
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
