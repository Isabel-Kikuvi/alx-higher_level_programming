#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import sys
import requests


if __name == "__main__":

    url = sys.argv[1]

    r = requests.post(url, data={'email': sys.argv[2]})
    print(r.text)
