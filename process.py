import pickle
from datetime import datetime as dt
import json


def unpickle_user():
    with open('user.json', 'rb') as user_file:
        return pickle.load(user_file)


def unpickle_repo():
    with open('repo.json', 'rb') as repo_file:
        return pickle.load(repo_file)


class Analysis():
    def __init__(self):
        self.data = unpickle_user()
        self.repo = unpickle_repo()

    def followers(self):
        follower_count = []
        for follower in self.data:
            follower_count.append(follower.get('followers'))
        print(follower_count)
        return follower_count

    def following(self):
        following_count = []
        for following in self.data:
            following_count.append(following.get('following'))
        print(following_count)
        return following_count

    def public_gists(self):
        public_gists_count = []
        for public_gists in self.data:
            public_gists_count.append(public_gists.get('public_gists'))
        print(public_gists_count)
        return public_gists_count

    def public_repos(self):
        public_repos_count = []
        for public_repos in self.data:
            public_repos_count.append(public_repos.get('public_repos'))
        print(public_repos_count)
        return public_repos_count

    def manage_created_at(self):
        for user in self.data:
             if self.get_created_at(user) != 0:
                pass            

    def get_created_at(self, user):
        """return timeedelta since the account was created"""
        for ind_user in self.data:
            if ind_user == user:
                py_created_at = dt.strptime(ind_user.get('created_at'),
                                        "%Y-%m-%dT%H:%M:%SZ")
                created_delta = dt.now() - py_created_at
                print(created_delta)
                return created_delta
            else:
                pass

    def manage_gh_index(self):
        gh_list = []
        for user in self.repo:
            user_repo_list = json.loads(self.repo[user])
            gh_list.append(self.get_gh_index(user, user_repo_list))
        print(gh_list)

    def get_gh_index(self, user, user_repo_list):
        # get the stargazers counts from the json
        repo_list = []
        count_list = []
        for repo in user_repo_list:
            for k, v in repo.items():
                if k == "stargazers_count" and v != 0:
                    repo_list.append(v)

        # sometimes there are no stars :(
        if repo_list == []:
            print("No stars found.")
            return
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
a.followers()
a.following()
a.public_gists()
a.public_repos()
a.manage_created_at()
a.manage_gh_index()
