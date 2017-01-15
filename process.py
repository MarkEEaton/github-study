import json
import pprint
from collections import Counter


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
        self.group = group

    def basic_data(self):
        """ assemble basic data """
        for user in self.data:
            login = user.get('login')
            self.output[login] = {"followers": user.get('followers'),
                                  "following": user.get('following'),
                                  "public_gists": user.get('public_gists'),
                                  "public_repos": user.get('public_repos'),
                                  "updated_at": user.get('updated_at'),
                                  "created_at": user.get('created_at'),
                                  "bio": user.get('bio')}

    def get_languages(self):
        """ count languages """
        language_counter = []
        for user in self.repo:
             for repo in self.repo[user]:
                 language_counter.append(repo['language'])
        return dict(Counter(language_counter))

    def stargazer(self):
        """ count stars per user """
        for user in self.data:
            stargazer = 0
            login = user.get('login')
            try:
                for repo in self.repo[login]:
                    stargazer += repo.get('stargazers_count')
            except KeyError:
                pass
            finally:
                self.output[login].update({"stargazers": stargazer})

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

    def sanity_check(self):
        """ gives data lengths to make sure we are on the right track """
        print(self.group + ' data: ' + str(len(self.data)) + '. \tOutput to json/processed' + self.group + '.json')
        print(self.group + ' repos: ' + str(len(self.repo)) + '. \tOutput to json/processed' + self.group + '.json')

librarians = Analysis('librarians')
randoms = Analysis('randoms')

if __name__ == "__main__":
    librarians.basic_data()
    librarians.stargazer()
    librarians.manage_gh_index()
    librarians.sanity_check()
    randoms.basic_data()
    randoms.stargazer()
    randoms.manage_gh_index()
    randoms.sanity_check()
    lang = {'librarians': librarians.get_languages(),
            'randoms': randoms.get_languages()}
    with open('json/processedlibrarians.json', 'w') as file1:
         json.dump(librarians.output, file1)
    with open('json/processedrandoms.json', 'w') as file2:
         json.dump(randoms.output, file2)
    with open('json/processedlanguages.json', 'w') as file3:
         json.dump(lang, file3)
