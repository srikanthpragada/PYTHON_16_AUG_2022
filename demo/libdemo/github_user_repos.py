import requests

resp = requests.get("https://api.github.com/users/gvanrossum/repos")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

repos = resp.json()   # Convert response(json) to dict

for repo in repos:
    print(repo['name'])
    print(repo['description'])
    print('-'  *  50)
