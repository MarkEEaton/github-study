import datetime as dt
import pprint

user_repos_to_delete = []

def thirty_days(data):
    """ manage the created_at comparison """
    for user in data:
        py_created_at = dt.datetime.strptime(user.get('created_at'),
                                "%Y-%m-%dT%H:%M:%SZ")
        created_delta = dt.datetime.now() - py_created_at
        if dt.timedelta(30) < created_delta:
            pass
        else:
            data.remove(user)
            user_repos_to_delete.append(user.get('login'))
            print("user created too recently: " + user.get('login'))
            print("user repos to delete: " + str(user_repos_to_delete))
    return data

def is_active(data):
    for user in data:
        py_updated_at = dt.datetime.strptime(user.get('updated_at'), "%Y-%m-%dT%H:%M:%SZ")
        updated_delta = dt.datetime.now() - py_updated_at
        if updated_delta > dt.timedelta(30):
            data.remove(user)
            user_repos_to_delete.append(user.get('login'))
            print("user removed due to inactivity: " + user.get('login'))
            print("user repos to delete: " + str(user_repos_to_delete))
    return data 


if __name__ == "__main__":
     import process
     thirty_days()
     is_active()
