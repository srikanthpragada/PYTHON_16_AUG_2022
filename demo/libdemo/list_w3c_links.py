import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
contents = resp.text

soup = BeautifulSoup(contents, 'html.parser')

links = []
for a in soup.find_all("a"):
    href = a['href']
    if 'void(0)' in href:
        continue

    if not href.startswith("http"):
        href = WEBSITE + href

    if href not in links:
        links.append(href)


for link in links:
    print(link)
