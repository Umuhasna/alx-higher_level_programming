#!/usr/bin/python3
'''
Docs
'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    param = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, param)

    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
