#!/usr/bin/python3
'''
Docs
'''
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    html = requests.get(url).text
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
