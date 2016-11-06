import datetime as dt
import json
import pprint


def unpickle_user():
    """" load the user data """
    with open('json/librarians_data.json', 'r') as user_file:
        return json.load(user_file)


def unpickle_repo():
    """ load the repo data """
    with open('json/librarians_repos.json', 'r') as repo_file:
        return json.load(repo_file)


class Analysis():
    def __init__(self):
        self.data = unpickle_user()
        self.repo = unpickle_repo()
        self.output = {} 

    def basic_data(self):
        """ print usernames """
        for follower in self.data:
            login = follower.get('login')
            self.output[login] = {"followers": follower.get('followers'),\
                   "following": follower.get('following'),\
                   "public_gists_count": follower.get('public_gists'),\
                   "public_repos": follower.get('public_repos')}

    def manage_gh_index(self):
        """ iterate through the users and return a list of gh indices """
        for user in self.repo:
            user_repo_list = self.repo[user]
            login = self.repo[user][0]['owner']['login']
            self.output[login].update({'gh-index': self.get_gh_index(user, user_repo_list)})
        pprint.pprint(self.output)

    def get_gh_index(self, user, user_repo_list):
        """ get the gh_index for a user """
        # get the stargazers counts from the json
        repo_list = []
        count_list = []
        for repo in user_repo_list:
            for k, v in repo.items():
                if k == "stargazers_count":
                    repo_list.append(v)

        # sometimes there are no stars :(
        if max(repo_list) == 0:
            return 0
        else:
            sorted_list = sorted(repo_list)

            # calculate the h-index
            for item in sorted_list:
                remaining_list = len(sorted_list[sorted_list.index(item):])
                if remaining_list > item:
                    count_list.append(item)
                elif remaining_list == item:
                    count_list.append(item)
                    break
                else:
                    while remaining_list < item:
                        item -= 1
                    else:
                        count_list.append(item)
                        break
            return(max(count_list))


a = Analysis()

if __name__ == "__main__":
    a.basic_data()
    a.manage_gh_index()
