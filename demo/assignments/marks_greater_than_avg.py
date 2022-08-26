# Program to accept marks of the students (stop when entered zero)
# print all those marks that are greater than the average

marks = []
while True:
    mark = int(input("Enter the marks [0 to stop]: "))
    if mark == 0:
        break
    marks.append(mark)

avg = sum(marks) / len(marks)
print(f'Marks greater than average {avg} are : ', end = '')
for n in sorted(marks):
    if n > avg:
        print(n, end=" ")
