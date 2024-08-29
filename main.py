import requests

target_url = "google.com"

def make_url(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

sub_list = []
with open("subdomainList.txt","r") as subdomainList:

    for sub in subdomainList:
        sub = sub.strip()
        url = "https://" + sub + "." + target_url
        response = make_url(url)
        if response:
            print("target url ---->" + url)