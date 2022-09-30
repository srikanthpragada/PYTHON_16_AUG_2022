from datetime import *

with open("tasks.txt", "rt") as f:
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 3:
            continue

        task = parts[0]
        try:
            sd = datetime.strptime(parts[1].strip(), "%d-%m-%Y")
            ed = datetime.strptime(parts[2].strip(), "%d-%m-%Y")
            days = (ed - sd).days
            print(f"{task:50}  {days:3}")
        except:
            pass




