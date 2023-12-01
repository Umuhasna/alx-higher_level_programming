#!/usr/bin/python3
'''
Docs
'''
from sys import argv
from requests import get


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]

    html = get(url, auth=(username, password))
    try:
        html_json = html.json()
        print(html_json.get('id'))
    except ValueError:
        print('Failed to retrieve ID')
