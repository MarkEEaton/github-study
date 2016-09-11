import datetime as dt
import pprint

def thirty_days(data):
    """ is the user active in the last 30 days? """
    py_created_at = dt.datetime.strptime(data[0]['created_at'],
                            "%Y-%m-%dT%H:%M:%SZ")
    created_delta = dt.datetime.now() - py_created_at
    if dt.timedelta(30) > created_delta:
        return data
    else:
        login = str(data[0]['actor']['login'])
        created_at = str(data[0]['created_at'])
        print("user removed due to inactivity: " + login + ' ' + created_at)
        return None 

def is_too_recent(data):
    py_created_at = dt.datetime.strptime(data['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    updated_delta = dt.datetime.now() - py_created_at
    if updated_delta < dt.timedelta(30):
        print("user was created too recently: " + str(data['login']) + " " + str(data['created_at']))
        return None
    else:
        return data 


if __name__ == "__main__":
     thirty_days()
     is_active()