'''WAP to accept basic salary from user and Give 10% of DA on basic salary ,12% HRA on basic salary
to employee if the salary is more than 50000 .calculate total salary.
'''

#getting the basic_salary from the user
basic_salary = int(input("Enter the basic salary: "))

#calculating basic_salary
#if basic_salary is greater than 50000 then add the DA 10% and HRA 12%
if basic_salary > 50000:
    da = 0.10 * basic_salary
    hra = 0.12 * basic_salary
else:
  da = 0
  hra = 0
total_salary = basic_salary + da + hra
print("The total salary is: ",total_salary)
