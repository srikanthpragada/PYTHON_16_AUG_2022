# Load data from JSON file to DB

import sqlite3
import json
import dbutil
from bs4 import BeautifulSoup

f = open("employees.xml", "rt")
contents = f.read()
f.close()

bs = BeautifulSoup(contents, "xml")

con = sqlite3.connect(dbutil.DBNAME)
cur = con.cursor()
count = 0
for employee in bs.find_all("employee"):

    try:
        name = employee.find("name").text.strip()
        job = employee.find("job").text.strip()
        salary = employee.find("salary").text.strip()

        cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                    (name, job, salary))
        count += 1
    except Exception as ex:
        print("Error -->", ex)

con.commit()
cur.close()
con.close()
print(f"Inserted {count} employees")
