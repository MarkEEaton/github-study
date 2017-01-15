import requests
import key
import pprint
import json
import re
import sys
import os

output = []

def search(url):
    """ make the api call; store data in output """
    global data_json, output, header_link
    data = requests.get(url, auth=(key.keyname, key.keysecret))
    data_json = data.json()['items']
    for user in data_json:
        output.append(user['login'])
    header_link = data.headers.get('link', None)

def loop(url):
    """ loop through the pages of results """
    global header_link
    search(url)
    while header_link:
        if re.search(r'; rel="next"', header_link):
            url = re.sub(r'.*<(.*)>; rel="next".*', r'\1', header_link)
            search(url)
        else:
            header_link = None

def find(keyword):
    url1 = "https://api.github.com/search/users?q={}&per_page=100&sort=joined&order=desc".format(keyword)
    url2 = "https://api.github.com/search/users?q={}&per_page=100&sort=joined&order=asc".format(keyword)
    loop(url1) # search descending
    loop(url2) # search ascending
    
    #for x in (sorted(set(output))):
    print(str(len(set(output))) + " librarians found.")

    return sorted(set(output))

if __name__ == "__main__":
    find("librarian")
