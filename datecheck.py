import datetime as dt
import pprint

def thirty_days(data):
    """ manage the created_at comparison """
    py_created_at = dt.datetime.strptime(data['created_at'],
                            "%Y-%m-%dT%H:%M:%SZ")
    created_delta = dt.datetime.now() - py_created_at
    if dt.timedelta(30) < created_delta:
        return data
    else:
        print("user created too recently: " + str(data['login']))
        return None 

def is_active(data):
    py_updated_at = dt.datetime.strptime(data['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
    updated_delta = dt.datetime.now() - py_updated_at
    if updated_delta > dt.timedelta(30):
        print("user removed due to inactivity: " + str(data['login']))
        return None
    else:
        return data 


if __name__ == "__main__":
     thirty_days()
     is_active()
