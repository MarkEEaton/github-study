import key
import pprint
import requests
import time
import json
import check
import random
import collections
import find_librarians
import pprint

filtered_users_librarians = []
filtered_users_randoms = []

# rate limit is 60 per hour for unauthenticated
# rate limit is 5000 per hour for authenticated

def header(number):
    """ create a header """
    print("---------------------------")
    print("*** " + number + " round filtering ***")
    print("---------------------------")

def generate_random():
    """ generates a list of random users and filters them. Ignores private repos """
    header("1st")
    while len(filtered_users_randoms) < 200:
        user = random.randint(1, 20000000)
        first_round(user, "randoms")

def generate_librarians():
    """ filters a list of librarians. Ignores private repos """
    header("1st")
    users = find_librarians.find("librarian")
    for user in users:
        first_round(user, "librarians")

def first_round(user, group):
    """ does the first round of filtering. user must have been active in the last 30 days """
    if isinstance(user, str):
        user_events = requests.get("https://api.github.com/users/{}/events".format(user), auth=(key.keyname, key.keysecret))
    elif isinstance(user, int):
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
            filtered_users_librarians.append(login)
            print('adding librarian user: ' + login + ' ' + created_at)
        elif check1 != None and group == "randoms":
            filtered_users_randoms.append(login)
            print('adding randoms user: ' + login + ' ' + created_at)

def second_round(group):
    """ does the second round of filtering. user account must be more than 30 days old """
    header("2nd")
    d = {'librarians': filtered_users_librarians,
         'randoms': filtered_users_randoms}
    data = d[group]
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

def third_round(data):
    header("3rd")
    print(len(data))
    data[:] = [x for x in data if x['bio'] != None]
    print(len(data))
    return data
 
def extractrepodata(data):
    """ gets json data on the users' repos """
    header("repo")
    repo_json = collections.OrderedDict() 
    for user in data:
        request_data = requests.get("https://api.github.com/users/{}/repos"
                                    .format(user['login']), auth=(key.keyname,
                                                         key.keysecret))
        check_rate_limit(request_data)
        if request_data.status_code != 200:
            print('error: ' + str(request_data.status_code))
        elif request_data.text == "[]":
            print(user['login'] + " no data from repo request")
            pass
        else:
            repo_json[user['login']] = request_data.json()
            print("adding " + user['login'] + " repos")
    return repo_json

def check_rate_limit(request_data):
    """ keeps track of rate limiting and sleeps when necessary """
    x = request_data.headers['x-ratelimit-remaining']
    print("request quota remaining: " + str(x) + "   ", end="")
    if int(x) < 20:
        print('sleeping...')
        time.sleep(300)
    else:
        pass

def store_it():
    """ stores the data for future use """
    with open('json/librarians_data.json', 'w') as f1, open('json/randoms_data.json', 'w') as f2:
        print(len(librarians_data))
        print(len(randoms_data))
        json.dump(librarians_data, f1)
        json.dump(randoms_data, f2)
    with open('json/librarians_repos.json', 'w') as f3, open('json/randoms_repos.json', 'w') as f4:
        json.dump(librarians_repos, f3)
        json.dump(randoms_repos, f4)

if __name__ == "__main__":
    generate_librarians()
    librarians_data = third_round(second_round("librarians"))
    generate_random()
    randoms_data = third_round(second_round("randoms"))
    librarians_repos = extractrepodata(librarians_data)
    randoms_repos = extractrepodata(randoms_data)
    store_it()
