import requests
import key
import re
import time

output = []


def search(url):
    """ make the api call; store data in output """
    global data, output, header_link
    data = []
    req = requests.get(url, auth=(key.keyname, key.keysecret))
    data.append(req.json())
    header_link = req.headers.get('link', None)


def loop(url):
    """ loop through the pages of results """
    global header_link
    search(url)
    while header_link:
        if re.search(r'; rel="next"', header_link):
            url = re.sub(r'.*<(.*)>; rel="next".*', r'\1', header_link)
            search(url)
        else:
            header_link = None
    for page in data:
        for user in page['items']:
            output.append(user['login'])


def find(keyword):
    print('waiting for search API, please be patient.')
    time.sleep(60)
    url1 = "https://api.github.com/search/users?q={}\
            &per_page=100&sort=joined&order=desc".format(keyword)
    url2 = "https://api.github.com/search/users?q={}\
            &per_page=100&sort=joined&order=asc".format(keyword)
    loop(url1)  # search descending
    loop(url2)  # search ascending

    print(str(len(set(output))) + " librarians found.")
    return sorted(set(output))

if __name__ == "__main__":
    find("librarian")
