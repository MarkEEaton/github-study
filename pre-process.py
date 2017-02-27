import json
import random
import pprint
from collections import Counter

with open('json/librarians_data.json', 'r') as a:
    ld = json.load(a)
with open('json/librarians_repos.json', 'r') as b:
    lr = json.load(b)
with open('json/randoms_data.json', 'r') as c:
    rd = json.load(c)
with open('json/randoms_repos.json', 'r') as d:
    rr = json.load(d)

ldf = [user for user in ld if (user['login'] in lr)]
rdf = [user for user in rd if (user['login'] in rr)]

# randomly reduce the randoms down to the size of the librarians
rdf_names = []
for user in rdf:
    rdf_names.append(user['login'])
rdf_names = rdf_names[:len(ldf)]

# check if a user is in rdf and if so add to a dict of repos
rrf = {user : value for user, value in rr.items() if (user in rdf_names)}  

# check if a user is in rdf and if so add to a list of users
rdf2 = [user for user in rd if (user['login'] in rdf_names)]

print(len(ldf))
print(len(lr))
print(len(rdf2))
print(len(rrf))

with open('json/pre-processedld.json', 'w') as e:
    json.dump(ldf, e)
with open('json/pre-processedlr.json', 'w') as f:
    json.dump(lr, f)
with open('json/pre-processedrd.json', 'w') as g:
    json.dump(rdf2, g)
with open('json/pre-processedrr.json', 'w') as h:
    json.dump(rrf, h)
