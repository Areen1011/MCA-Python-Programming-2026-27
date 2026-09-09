basic_salary = int(input("Enter the basic salary of the employee: "))

da = basic_salary * 0.20
hra = basic_salary * 0.15
gross_salary = basic_salary + da + hra
tax_deduction = gross_salary * 0.10
net_salary = gross_salary - tax_deduction

print("Basic Salary: ", basic_salary)
print("Dearness Allowance (DA): ", da)
print("House Rent Allowance (HRA): ", hra)
print("Gross Salary: ", gross_salary)
print("Tax Deducted: ", tax_deduction)
print("Net Salary: ", net_salary)
