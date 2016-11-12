import json
import pprint


def load_user(file):
    """" load the user data """
    with open(file, 'r') as user_file:
        return json.load(user_file)


def load_repo(file):
    """ load the repo data """
    with open(file, 'r') as repo_file:
        return json.load(repo_file)


class Analysis():
    def __init__(self, group):
        self.data = load_user('json/' + group + '_data.json')
        self.repo = load_repo('json/' + group + '_repos.json')
        self.output = {}

    def basic_data(self):
        """ assemble basic data """
        for follower in self.data:
            login = follower.get('login')
            self.output[login] = {"followers": follower.get('followers'),
                                  "following": follower.get('following'),
                                  "public_gists": follower.get('public_gists'),
                                  "public_repos": follower.get('public_repos')}

    def manage_gh_index(self):
        """ iterate through the users and return a list of gh indices """
        for user in self.repo:
            login = self.repo[user][0]['owner']['login']
            self.output[login].update({'gh-index':
                                       self.get_gh_index(user,
                                                         self.repo[user])})

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


librarians = Analysis('librarians')
randoms = Analysis('randoms')

if __name__ == "__main__":
    librarians.basic_data()
    librarians.manage_gh_index()
    randoms.basic_data()
    randoms.manage_gh_index()
    with open('json/processedlibrarians.json', 'w') as file1:
         json.dump(librarians.output, file1)
    with open('json/processedrandoms.json', 'w') as file2:
         json.dump(randoms.output, file2)
