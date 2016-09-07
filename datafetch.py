import key
import requests
import time
import json

users = ['markeeaton', 'robincamille', 'samuelclay', 'timtomch', 'szweibel', 'blah']

# rate limit is 60 per hour for unauthenticated
# rate limit is 5000 per hour for authenticated


def extractuserdata():
    """ gets json data on the users """
    user_json = []
    url = "https://api.github.com/users/{}"
    for user in users:
        request_data = requests.get(url.format(user),
                                    auth=(key.keyname, key.keysecret))
        if request_data.status_code != 200:
            print('error: ' + str(request_data.status_code))
        check_rate_limit(request_data)
        user_json.append(request_data.json())
    return user_json


def extractrepodata():
    """ gets json data on the users' repos """
    repo_json = {}

    for user in users:
        request_data = requests.get("https://api.github.com/users/{}/repos"
                                    .format(user), auth=(key.keyname,
                                                         key.keysecret))
        check_rate_limit(request_data)
        if request_data.status_code != 200:
            print('error: ' + str(request_data.status_code))
        elif request_data.text == "[]":
            print("no data from repo request")
            pass
        else:
            repo_json.update({user: request_data.text})
    return repo_json


def pickleit():
    """ stores the data for future use """
    with open('user.json', 'w') as f1, open('repo.json', 'w') as f2:
        json.dump(extractuserdata(), f1)
        json.dump(extractrepodata(), f2)


def check_rate_limit(request_data):
    """ keeps track of rate limiting and sleeps when necessary """
    x = request_data.headers['x-ratelimit-remaining']
    print("request quota remaining: " + str(x))
    if int(x) < 3:
        print('sleeping...')
        time.sleep(300)
    else:
        pass

if __name__ == "__main__":
    extractuserdata()
    extractrepodata()
    pickleit()
