#!/usr/bin/python3
'''
Docs
'''
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    url = argv[1]

    try:
        req = request.Request(url)
        with request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print(html)
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
