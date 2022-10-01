from datetime import *

tasks = []
with open("tasks.txt", "rt") as f:
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:  # Not enough entries
            continue  # ignore line

        task = parts[0]  # take text
        try:
            sd = datetime.strptime(parts[1].strip(), "%d-%m-%Y")
        except:
            continue   # Conversion error, so skip line

        if len(parts) > 2:
            try:
                ed = datetime.strptime(parts[2].strip(), "%d-%m-%Y")
                days = (ed - sd).days
            except:
                continue # Conversion error, so skip line
        else:
            days = 'Incomplete'

        tasks.append((task, days))


for text, days in sorted(tasks):
    print(f"{text:50} {days}")
