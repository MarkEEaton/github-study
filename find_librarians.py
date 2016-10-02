import requests
import key
import pprint
import json
import re

users = requests.get("https://api.github.com/search/users?q=librarian&per_page=100", auth=(key.keyname, key.keysecret))
users_json = users.json()
users_list = users_json['items']
header_link = users.headers.get('link', None)

while header_link:
    if re.search(r'; rel="next"', header_link):
        next_page = re.sub(r'.*<(.*)>; rel="next".*', r'\1', header_link)
        more_data = requests.get(next_page, auth=(key.keyname, key.keysecret))
        more_json = more_data.json()
        more_list = more_json['items']
        users_list = users_list + more_list 
        break
    else:
        header_link = None

#pprint.pprint(users_json)

print(len(users_list))

#for user in users_json['items']:
    #print(user)
    #print(user['login'])
