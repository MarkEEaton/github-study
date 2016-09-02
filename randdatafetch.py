import json
import requests
import pickle
import random
import pprint
import key

users = random.sample(range(1, 20000000), 20)

def extractuserdata():
    """generate json of x random users"""
    userjson = []

    def usergen():
        """generator to add a new random user"""
        user = random.randint(1, 20000000)
        yield requests.get("https://api.github.com/user/{}".format(user), auth=(key.keyname, key.keysecret))

    while len(userjson) <= 2:
        # need to add logic to test if user returns is legit
        userjson.append(json.loads(next(usergen()).text))

    pp = pprint.PrettyPrinter()
    pp.pprint(userjson)
    return userjson

def extractrepodata():
    repodata = []
    repojson = []

    for user in users:
        repodata.append(requests.get("https://api.github.com/user/{}/repos".format(user), auth=(key.keyname, key.keysecret)))

    for user in repodata:
        repojson.append(json.loads(user.text))

 #   print(repojson)
    return repojson

def pickleit():
    f1 = open('randuser.json', 'wb')
    f2 = open('randrepo.json', 'wb')
    pickle.dump(extractuserdata(), f1)
    pickle.dump(extractrepodata(), f2)
    f1.close()
    f2.close()

pickleit()
