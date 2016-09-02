import json
import pprint
import key
import requests
import pickle
import time

users = ['markeeaton', 'robincamille', 'samuelclay', 'timtomch', 'szweibel']

# rate limit is 60 per hour for unauthenticated
# rate limit is 5000 per hour for authenticated

def extractuserdata():
    user_json = []
    url = "https://api.github.com/users/{}"
    for user in users:
        request_data = requests.get(url.format(user), auth=(key.keyname, key.keysecret))
        print(type(request_data))
        if request_data.status_code != 200:
            print('error: ' + str(request_data.status_code))
        check_rate_limit(request_data)
        user_json.append(request_data.json())
    return user_json

def extractrepodata():
    repo_data = []
    repo_json = {} 

    for user in users:
        request_data = requests.get("https://api.github.com/users/{}/repos".format(user), auth=(key.keyname, key.keysecret))
        check_rate_limit(request_data)
        if request_data.status_code != 200:
            print('error: ' + str(request_data.status_code))
        repo_json.update({user: request_data.text})
    return repo_json


def pickleit():
    f1 = open('user.json', 'wb')
    f2 = open('repo.json', 'wb')
    pickle.dump(extractuserdata(), f1)
    pickle.dump(extractrepodata(), f2)
    f1.close()
    f2.close()

def check_rate_limit(request_data):
    x = request_data.headers['x-ratelimit-remaining']
    print("request quota remaining: " + str(x))
    if x < 3:
        print('sleeping...')
        time.sleep(300)
    else:
        pass

if __name__ == "__main__":
    extractuserdata()
    extractrepodata()
    pickleit()
