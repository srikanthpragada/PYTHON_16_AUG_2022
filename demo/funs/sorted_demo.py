nums = [10, -20, 30, -5, 50]

for n in sorted(nums, key=abs):
    print(n)

names = ['Java', 'Python', 'C++', 'Unix', 'Pascal', 'Cobol']

for n in sorted(names, key=len):
    print(n)

persons = [{'name': 'Scott', 'age': 40},
           {'name': 'Tom', 'age': 45},
           {'name': 'Dave', 'age': 30},
           {'name': 'Larry', 'age': 20}]


def get_age(d: dict) -> int:
    return d['age']


for p in sorted(persons, key=get_age, reverse=True):
    print(f"{p['name']:20} {p['age']:2}")
