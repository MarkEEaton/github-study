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
ldf = [user for user in ld if (user['login'] in lr)]
rdf = [user for user in rd if (user['login'] in rr)]

# randomly reduce the randoms down to the size of the librarians
rdf_names = []
for user in rdf:
    rdf_names.append(user['login'])
rdf_names = rdf_names[:len(ldf)]

rrf = [user for user in rr.keys() if (user in rdf_names)]
rdf2 = [user for user in rd if (user['login'] in rdf_names)]

print(len(ldf))
print(len(lr))
print(len(rdf2))
print(len(rrf))
