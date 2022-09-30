import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

details = resp.json()   # Convert response(json) to dict
print(details['name'])
print(details['company'])
print(details['followers'])
