#!/usr/bin/python3
'''
Docs
'''
from sys import argv
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""

    html = requests.post(url, data={'q': letter})
    try:
        html_json = html.json()
        if html_json:
            json_id = html_json.get('id')
            json_name = html_json.get('name')
            print('[{}] {}'.format(json_id, json_name))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
