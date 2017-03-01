import json
import random
from collections import Counter
from jsontriage import triage

with open('json/librarians_data.json', 'r') as a:
    ld = json.load(a)
with open('json/librarians_repos.json', 'r') as b:
    lr = json.load(b)
with open('json/randoms_data.json', 'r') as c:
    rd = json.load(c)
with open('json/randoms_repos.json', 'r') as d:
    rr = json.load(d)

# reduce librarians data down to the size of librarians repos
ldf = [user for user in ld if (user['login'] in lr)]

# reduce randoms data down to the size of randoms repos
rdf = [user for user in rd if (user['login'] in rr)]

# manually do triage of librarians / non-librarians
print('Librarians before triage: ' + str(len(ldf)))
ldf = triage(ldf)
print('Librarians after triage: ' + str(len(ldf)))

# reduce librarians repos down to the size of triaged librarians
ldf_names = []
for user in ldf:
    ldf_names.append(user['login'])
lrf = {user : value for user, value in lr.items() if (user in ldf_names)}

# randomly reduce the randoms down to the size of the librarians
rdf_names = []
for user in rdf:
    rdf_names.append(user['login'])
rdf_names = rdf_names[:len(ldf)]

# reduce random repos to the length of rdf_names 
rrf = {user : value for user, value in rr.items() if (user in rdf_names)}  

# reduce random users to the length of rdf_names 
rdf2 = [user for user in rd if (user['login'] in rdf_names)]

# remove duplicates in rdf2
rdf3 = []
for x in rdf2:
    if x not in rdf3:
        rdf3.append(x)

print('Length of librarians data: ' + str(len(ldf)))
print('Length of librarians repos: ' + str(len(lrf)))
print('Length of randoms data: ' + str(len(rdf3)))
print('Length of randoms repos: ' + str(len(rrf)))

with open('json/pre-processedld.json', 'w') as e:
    json.dump(ldf, e)
with open('json/pre-processedlr.json', 'w') as f:
    json.dump(lr, f)
with open('json/pre-processedrd.json', 'w') as g:
    json.dump(rdf3, g)
with open('json/pre-processedrr.json', 'w') as h:
    json.dump(rrf, h)
