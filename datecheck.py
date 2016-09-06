import datetime as dt
import process
import pprint

output_users = []

def manage_is_thirty_days():
    """ manage the created_at comparison """
    for user in process.a.data:
        if dt.timedelta(30) < get_thirty_days(user):
            print("pass")
            output_users.append(user)
        else:
            print("fail") 
    return(output_users)

def get_thirty_days(user):
    """return timeedelta since the account was created"""
    py_created_at = dt.datetime.strptime(user.get('created_at'),
                            "%Y-%m-%dT%H:%M:%SZ")
    created_delta = dt.datetime.now() - py_created_at
    return created_delta

"""
def is_active(user):
    for ind_user in process.a.data:
        if ind_user == user:
            #py_last_active = 
            pass
"""

if __name__ == "__main__":
     pprint.pprint(manage_is_thirty_days())
