#!/usr/bin/python3
"""
Take in a URL, sends a request to the URL
Display the value of the X-Request-Id variable,
found in the header of the response
"""
import sys
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        headers = resp.getheaders()
        soln = resp.getheader('X-Request-Id')
        print(soln)
