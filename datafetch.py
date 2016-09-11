import key
import pprint
import requests
import time
import json
import datecheck
import random

users = ['markeeaton', 'robincamille', 'samuelclay', 'timtomch', 'szweibel', 'blah']
filtered_users = []

# rate limit is 60 per hour for unauthenticated
# rate limit is 5000 per hour for authenticated

def generate_users():
    """ generates a list of users and filters them """

    while len(filtered_users) < 2:
        user = random.randint(1, 20000000)
        user_events = requests.get("https://api.github.com/user/{}/events".format(user), auth=(key.keyname, key.keysecret))
        check_rate_limit(user_events)
        if user_events.status_code != 200:
            print('error: ' + str(user_events.status_code))
            pass
        elif user_events.text == "[]":
            print('no repos. passing')
            pass
        else:
            login = str(json.loads(user_events.text)[0]['actor']['login'])
            created_at = str(json.loads(user_events.text)[0]['created_at'])
            check1 = datecheck.thirty_days(json.loads(user_events.text))
            #check2 = datecheck.is_active(json.loads(user_events.text))
            #if check1 and check2 != None:
            if check1 != None:
                filtered_users.append(user_events.json())
                print('adding user: ' + login + ' ' + created_at)
            else:
                pass            
        
"""
    return filtered_users
"""

def extractuserdata():
    """ gets json data on the users """
    user_json = []
    url = "https://api.github.com/users/{}"
    for user in users:
        request_data = requests.get(url.format(user),
                                    auth=(key.keyname, key.keysecret))
        if request_data.status_code != 200:
            print('error: ' + str(request_data.status_code))
        pprint.pprint(request_data.text)
        check_rate_limit(request_data)
        check1 = datecheck.thirty_days(json.loads(request_data.text))
        check2 = datecheck.is_active(json.loads(request_data.text))
        if check1 and check2 != None:
            user_json.append(request_data.json())
        else:
            pass
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
    pprint.pprint(json.loads(repo_json['markeeaton']))
    print(type(repo_json['markeeaton']))
    return repo_json


def pickleit():
    """ stores the data for future use """
    with open('user.json', 'w') as f1, open('repo.json', 'w') as f2:
        json.dump(extractuserdata(), f1)
        json.dump(extractrepodata(), f2)


def check_rate_limit(request_data):
    """ keeps track of rate limiting and sleeps when necessary """
    x = request_data.headers['x-ratelimit-remaining']
    print("request quota remaining: " + str(x) + "   ", end="")
    if int(x) < 3:
        print('sleeping...')
        time.sleep(300)
    else:
        pass

if __name__ == "__main__":
    #extractuserdata()
    #extractrepodata()
    generate_users()
    #pickleit()
