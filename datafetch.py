import json
import pprint
import key
import requests
import pickle

users = ['markeeaton', 'robincamille', 'samuelclay', 'timtomch', 'szweibel']


def extractuserdata():
    url = "https://api.github.com/users/{}"
    return [json.loads(requests.get(url.format(user)).text) for user in users]


def extractrepodata():
    repo_data = []
    repo_json = {} 

    for user in users:
        request_data = requests.get("https://api.github.com/users/{}/repos".format(user), auth=(key.keyname, key.keysecret))
        repo_json.update({user: json.loads(request_data.text)})

    pprint.pprint(repo_json)
    return repo_json


def pickleit():
    f1 = open('user.json', 'wb')
    f2 = open('repo.json', 'wb')
    pickle.dump(extractuserdata(), f1)
    pickle.dump(extractrepodata(), f2)
    f1.close()
    f2.close()

if __name__ == "__main__":
    extractuserdata()
    extractrepodata()
    pickleit()
