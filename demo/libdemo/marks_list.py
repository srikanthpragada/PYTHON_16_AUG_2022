f = open("students.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue  # ignore line

    name, *marks = parts  # Unpacking

    valid_marks = list(filter(str.isdigit, marks))
    total = sum(map(int, valid_marks))
    avg = total / len(valid_marks)
    print(f"{name:20} {total:3} {avg:5.2f}")

f.close()
