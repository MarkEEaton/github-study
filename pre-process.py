import json
import random
from collections import Counter

with open('json/librarians_data.json', 'r') as a:
    ld = json.load(a)
with open('json/librarians_repos.json', 'r') as b:
    lr = json.load(b)
with open('json/randoms_data.json', 'r') as c:
    rd = json.load(c)
with open('json/randoms_repos.json', 'r') as d:
    rr = json.load(d)

# if user is not in the repolist, remove it
for user in ld:
    if user['login'] in lr:
        pass
    else:
        ld.remove(user)

# same for randoms
for user in rd:
    if user['login'] in rr:
        pass
    else:
        rd.remove(user)


### randomly reduce the randoms down to the size of the librarians
rd_names = []

# create user lists
for user in rd:
    rd_names.append(user['login'])
rd_names = rd_names[:69]

for user in rr.keys():
    if user in rd_names:
        pass
    else:
        rr.pop(user)

for user in rd:
    for k, v in user.items():
        if k == 'login':
            if v in rd_names:
                pass
            else:
                rd.pop(user)

print(len(rd))
