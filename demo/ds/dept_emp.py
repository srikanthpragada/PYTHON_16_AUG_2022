data = [('IT', 'James'), ('HR', 'Scott'), ('HR', 'Larry'), ('IT', 'Bill'), ('PR', 'Steve'), ('IT', 'Andy')]
depts = {}
for entry in data:
    dname, ename = entry
    # employees = depts.get(dname, [])
    # employees.append(ename)
    # depts[dname] = employees

    if dname in depts:
        depts[dname].append(ename)
    else:
        depts[dname] = [ename]


for dname, employees in sorted(depts.items()):
    print(f"{dname}  {','.join(employees)}")



