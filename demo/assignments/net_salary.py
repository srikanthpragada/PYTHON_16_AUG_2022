# Take basic salary and display net salary by adding HRA @ 30% and DA @ 20%

basic = float(input("Enter Basic salary: "))
hra = basic * 0.3
da = basic * 0.2
net_salary = basic + hra + da
print(f"Basic Salary   {basic:10.2f}")
print(f"HRA            {hra:10.2f}")
print(f"DA             {da:10.2f}")
print(f"Net salary     {net_salary:10.2f}")
