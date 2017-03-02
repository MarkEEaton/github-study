import datetime as dt


def ninety_days(data):
    """ is the user active in the last 90 days? """
    py_updated_at = dt.datetime.strptime(data['updated_at'],
                                         "%Y-%m-%dT%H:%M:%SZ")
    updated_delta = dt.datetime.now() - py_updated_at
    if dt.timedelta(90) > updated_delta:
        return data
    else:
        login = str(data['login'])
        updated_at = str(data['updated_at'])
        print("user removed due to inactivity: " + login + ' ' + updated_at)
        return None


def is_too_recent(data):
    """ is the users account created more than 30 days ago? """
    py_created_at = dt.datetime.strptime(data['created_at'],
                                         "%Y-%m-%dT%H:%M:%SZ")
    created_delta = dt.datetime.now() - py_created_at
    if created_delta < dt.timedelta(30):
        print("user was created too recently: " + str(data['login'])
              + " " + str(data['created_at']))
        return None
    else:
        return data
