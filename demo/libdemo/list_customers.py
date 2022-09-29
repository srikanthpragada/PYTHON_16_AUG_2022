import re

with open("customers.txt", "rt") as f:
    customers = {}
    for line in f.readlines():
        # find name
        m = re.search("[A-Za-z ]+", line)
        if m is None:
            continue

        name = m.group().strip()  # Take match and get rid of leading and trailing spaces

        if len(name) == 0:
            continue

        # Find number
        m = re.search(r"\d+", line)
        if m is None:
            continue

        mobile = m.group()
        customers[name] = mobile

for name, mobile in sorted(customers.items()):
    print(f"{name:20}  {mobile}")
