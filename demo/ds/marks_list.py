data = [(1, 69), (2, 80), (1, 89), (2, 78), (3, 60), (4, 90), (6, 50), (5, 88)]

marks = {}

for d in data:
    rollno, mark = d
    total = marks.get(rollno, 0)
    marks[rollno] = total + mark

for rollno, total in sorted(marks.items()):
    print(f"{rollno:3}  {total:3}")
