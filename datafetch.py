import json
import requests
import pickle

users = ['markeeaton', 'robincamille', 'samuelclay', 'timtomch', 'szweibel']


def extractuserdata():
    url = "https://api.github.com/users/{}"
    return [json.loads(requests.get(url.format(user)).text) for user in users]


def extractrepodata():
    repodata = []
    repojson = []

    for user in users:
        repodata.append(requests.get("https://api.github.com/users/{}/repos".format(user)))

    for user in repodata:
        repojson.append(json.loads(user.text))

    return repojson


def pickleit():
    f1 = open('user.json', 'wb')
    f2 = open('repo.json', 'wb')
    pickle.dump(extractuserdata(), f1)
    pickle.dump(extractrepodata(), f2)
    f1.close()
    f2.close()
