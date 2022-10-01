from datetime import *


class Task:
    def __init__(self, text, start, end=None):
        self.text = text
        self.start = start
        self.end = end

    @property
    def days(self):
        if self.end is None:
            return f"{(datetime.now() - self.start).days} I"
        else:
            return f"{(self.end - self.start).days} C"

    @property
    def startdate(self):
        return self.start.strftime("%d-%m-%Y")

    def __lt__(self, other):
        return self.start < other.start  # Compare by start date


tasks = []
with open("tasks.txt", "rt") as f, open("taskslog.txt", "wt") as log:
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:  # Not enough entries
            log.write(f"Incomplete  - {line.strip()}\n")
            continue  # ignore line

        text = parts[0]  # take text
        try:
            sd = datetime.strptime(parts[1].strip(), "%d-%m-%Y")
        except:
            log.write(f"Start date conversion failed  - {parts[1].strip()}\n")
            continue  # Conversion error, so skip line

        if len(parts) > 2:
            try:
                ed = datetime.strptime(parts[2].strip(), "%d-%m-%Y")
                task = Task(text, sd, ed)
            except:
                log.write(f"End date conversion failed  - {parts[2].strip()}\n")
                continue  # Conversion error, so skip line
        else:
            task = Task(text, sd)

        tasks.append(task)

for task in sorted(tasks):
    print(f"{task.text:50} {task.startdate:10} {task.days}")
