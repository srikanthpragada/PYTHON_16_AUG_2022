# Program to accept Basic salary and Grade (either 1 or 2).
# Calculate and Display Net salary on the basis of grade
# Condition: if Grade = 1: HRA @ 30% DA @ 20%
#            if Grade = 2: HRA @ 25% DA @ 10%

basic = int(input("Enter Basic Salary  : "))
grade = int(input("Enter Grade (1 or 2): "))

if grade == 1:
    hra = basic * 0.30
    da = basic * 0.20
else:
    hra = basic * 0.25
    da = basic * 0.15

net_salary = basic + hra + da

print(f"Basic Salary           {basic:10.2f}")
print(f"HRA                    {hra:10.2f}")
print(f"DA                     {da:10.2f}")
print(f"Net Salary             {net_salary:10.2f}")
