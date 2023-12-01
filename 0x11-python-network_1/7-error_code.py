#!/usr/bin/python3
'''
Docs
'''
from sys import argv
from requests.exceptions import HTTPError
import requests


if __name__ == "__main__":
    url = argv[1]

    try:
        html = requests.get(url)

        html.raise_for_status()
        print(html.text)
    except HTTPError as e:
        print('Error code: {}'.format(e.html.status_code))
