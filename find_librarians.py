import requests
import key
import pprint
import json
import re
import sys
import os

""" finds up to 2000 results: 1000 ascending and 1000 descending """

if len(sys.argv) < 2:
    sys.exit('Usage: python find_librarians.py <file>')
 
if os.path.exists(".//json//" + sys.argv[1] + ".json"):
    sys.exit("Error: can't write a file for this search term. Already exists.")

search_term = sys.argv[1]

url1 = "https://api.github.com/search/users?q={}&per_page=100&sort=joined&order=desc".format(search_term)
url2 = "https://api.github.com/search/users?q={}&per_page=100&sort=joined&order=asc".format(search_term)
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

loop(url1) # search descending
loop(url2) # search ascending

output = set(output)

for x in (sorted(output)):
    print(x)
print(str(len(output)) + " users found.")
