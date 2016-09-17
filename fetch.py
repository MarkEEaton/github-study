import key
import pprint
import requests
import time
import json
import check
import random
import collections

users = ['markeeaton', 'robincamille', 'samuelclay', 'timtomch', 'szweibel', 'blah']
filtered_users_librarians = []
filtered_users_randoms = []
#filtered_users_logins = []

# rate limit is 60 per hour for unauthenticated
# rate limit is 5000 per hour for authenticated

def header(number):
    print("---------------------------")
    print("*** " + number + " round filtering ***")
    print("---------------------------")

def generate_random():
    """ generates a list of random users and filters them. Ignores private repos """
    header("1st")
    while len(filtered_users_randoms) < 10:
        user = random.randint(1, 20000000)
        first_round(user, "randoms")

def generate_librarians():
    header("1st")
    for user in users:
        first_round(user, "librarians")

def first_round(user, group):
    if type(user) == str:
        user_events = requests.get("https://api.github.com/users/{}/events".format(user), auth=(key.keyname, key.keysecret))
    elif type(user) == int:
        user_events = requests.get("https://api.github.com/user/{}/events".format(user), auth=(key.keyname, key.keysecret))
    check_rate_limit(user_events)
    if user_events.status_code != 200:
        print('error: ' + str(user_events.status_code))
        pass
    elif user_events.text == "[]":
        print('no repos. passing.')
        pass
    else:
        login = str(json.loads(user_events.text)[0]['actor']['login'])
        created_at = str(json.loads(user_events.text)[0]['created_at'])
        check1 = check.thirty_days(json.loads(user_events.text))
        if check1 != None and group == "librarians":
            #filtered_users_librarians.append(user_events.json())
            filtered_users_librarians.append(login)
            print('adding librarian user: ' + login + ' ' + created_at)
            return
        elif check1 != None and group == "randoms":
            #filtered_users_randoms.append(user_events.json())
            filtered_users_randoms.append(login)
            print('adding randoms user: ' + login + ' ' + created_at)
            return
        else:
            return            
        

def second_round(group):
    """ gets json data on the users """
    header("2nd")
    if group == "librarians":
        data = filtered_users_librarians
    elif group == "randoms":
        data = filtered_users_randoms
    else:
        print("undefined group")
    user_json = []
    url = "https://api.github.com/users/{}"
    for user in data:
        request_data = requests.get(url.format(user),
                                    auth=(key.keyname, key.keysecret))
        check_rate_limit(request_data)
        if request_data.status_code != 200:
            print('error: ' + str(request_data.status_code))
        elif request_data.text == "[]":
            print('no data. passing.')
        else:
            login = str(json.loads(request_data.text)['login'])
            created_at = str(json.loads(request_data.text)['created_at'])
            check2 = check.is_too_recent(json.loads(request_data.text))
            if check2 != None:
                user_json.append(request_data.json())
                print('adding ' + group + ' user: ' + login + ' ' + created_at)
            else:
                pass
    return user_json


def extractrepodata():
    """ gets json data on the users' repos """
    repo_json = collections.OrderedDict() 

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
    with open('librarians_data.json', 'w') as f1, open('randoms_data.json', 'w') as f2:
        json.dump(librarians_data, f1)
        json.dump(randoms_data, f2)


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
    #extractrepodata()
    generate_librarians()
    librarians_data = second_round("librarians")
    generate_random()
    randoms_data = second_round("randoms")
    pickleit()
