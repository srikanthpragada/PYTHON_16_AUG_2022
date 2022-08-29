data = [('IT', 'James', 'Prog'), ('HR', 'Scott', 'Manager'),
        ('HR', 'Larry', 'Manager'), ('IT', 'Bill', 'DBA'), ('PR', 'Steve', 'Eng'),
        ('IT', 'Andy', "QA")]

depts = {}
for entry in data:
    dname, ename, job = entry
    # employees = depts.get(dname, [])
    # employees.append(ename)
    # depts[dname] = employees2

    if dname in depts:
        depts[dname].append((ename, job))
    else:
        depts[dname] = [(ename, job)]

for dname, employees in sorted(depts.items()):
    print(f"{dname}")
    for e in employees:
        print(f"{e[0]:20} {e[1]}")
