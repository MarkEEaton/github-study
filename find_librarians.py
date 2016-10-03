import requests
import key
import pprint
import json
import re

url = "https://api.github.com/search/users?q=library&per_page=100&sort=joined&order=desc"
output = []
output_json = []

def search(url):
    data = requests.get(url, auth=(key.keyname, key.keysecret))
    data_json = data.json()['items']
    print(data.json()['total_count'])
    global output, output_json, header_link
    output_json = output_json + data_json
    for user in data_json:
        output.append(user['login'])
    header_link = data.headers.get('link', None)

search(url)

while header_link:
    if re.search(r'; rel="next"', header_link):
        url = re.sub(r'.*<(.*)>; rel="next".*', r'\1', header_link)
        search(url)
    else:
        header_link = None

print(len(output_json))
print(output)
