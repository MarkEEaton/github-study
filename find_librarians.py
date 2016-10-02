import requests
import key
import pprint
import json
import re

url = "https://api.github.com/search/users?q=library&per_page=100"
output = []

def search(url):
    data = requests.get(url, auth=(key.keyname, key.keysecret))
    data_json = data.json()['items']
    global output, header_link
    output = output + data_json
    header_link = data.headers.get('link', None)

search(url)

while header_link:
    if re.search(r'; rel="next"', header_link):
        url = re.sub(r'.*<(.*)>; rel="next".*', r'\1', header_link)
        search(url)
    else:
        header_link = None

#pprint.pprint(users_json)

print(len(output))

#for user in users_json['items']:
    #print(user)
    #print(user['login'])
