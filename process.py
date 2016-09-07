import datetime as dt
import json
import datecheck 


def unpickle_user():
    """" load the user data """
    with open('user.json', 'r') as user_file:
        return json.load(user_file)


def unpickle_repo():
    """ load the repo data """
    with open('repo.json', 'r') as repo_file:
        return json.load(repo_file)


class Analysis():
    def __init__(self):
        self.data = unpickle_user()
        self.repo = unpickle_repo()

    def followers(self):
        """ get a list of follower counts """
        follower_count = []
        for follower in self.data:
            follower_count.append(follower.get('followers'))
        print(follower_count)
        return follower_count

    def following(self):
        """ get a list of following counts """
        following_count = []
        for following in self.data:
            following_count.append(following.get('following'))
        print(following_count)
        return following_count

    def public_gists(self):
        """ get a list of public gist counts """
        public_gists_count = []
        for public_gists in self.data:
            public_gists_count.append(public_gists.get('public_gists'))
        print(public_gists_count)
        return public_gists_count

    def public_repos(self):
        """ get a list of public repo counts """
        public_repos_count = []
        for public_repos in self.data:
            public_repos_count.append(public_repos.get('public_repos'))
        print(public_repos_count)
        return public_repos_count

    def manage_gh_index(self):
        """ iterate through the users and return a list of gh indices """
        gh_list = []
        for user in self.repo:
            user_repo_list = json.loads(self.repo[user])
            gh_list.append(self.get_gh_index(user, user_repo_list))
        print(gh_list)

    def get_gh_index(self, user, user_repo_list):
        """ get the gh_index for a user """
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
checked_data = datecheck.thirty_days(datecheck.is_active(a.data))

if __name__ == "__main__":
    a.followers()
    a.following()
    a.public_gists()
    a.public_repos()
    a.manage_gh_index()
