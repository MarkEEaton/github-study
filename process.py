import pickle
import datetime
import pprint
import datafetch


def unpickle_user():
    user_json = pickle.load(open('user.json', 'rb'))
    return user_json

def unpickle_repo():
    repo_json = pickle.load(open('repo.json', 'rb'))
    pprint.pprint(repo_json)
    return repo_json



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

    def created_at(self):
        """return timeedelta since the account was created"""
        created_at_count = []
        for created_at in self.data:
            py_created_at = datetime.datetime.strptime(created_at.get('created_at'), "%Y-%m-%dT%H:%M:%SZ")
            created_delta = datetime.datetime.now() - py_created_at
            created_at_count.append(created_delta)
        print(created_at_count)
        return created_at_count

    def get_gh_index(self, user):
        # get the stargazers counts from the json
        repo_list = []
        count_list = []
        for user in self.repo:
            for repo in user:
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
            print(str(max(count_list)))
            return



a = Analysis()
a.followers()
a.following()
a.public_gists()
a.public_repos()
a.created_at()
a.get_gh_index(user)
