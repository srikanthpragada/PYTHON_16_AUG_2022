import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

countries = resp.json()

for country in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    name = country['name']['common']
    capital = country.get('capital', ['Unknown'])[0]
    population = country['population']
    area = country['area']

    print(f"{name:50} {capital:20} {population:10} {area:10}")
