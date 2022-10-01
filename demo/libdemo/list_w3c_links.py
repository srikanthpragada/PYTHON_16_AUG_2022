import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.w3schools.com/")
contents = resp.text

soup = BeautifulSoup(contents, 'html.parser')

for a in soup.find_all("a"):
    href = a['href']
    if 'void(0)' not in href:
        print(a['href'])
