import json
import random

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

for user in rd:
    if user['login'] in rr:
        pass
    else:
        rd.remove(user)


# randomly reduce the randoms down to the size of the librarians
rd_list = []
rr_list = []

for user in rd:
    rd_list.append(user['login'])
for user in rr.keys():
    rr_list.append(user)

rr_list = random.sample(rr_list, 69)

final_list = []

for user in rd_list:
    if user in rr_list:
        final_list.append(user) 
    else:
        pass

