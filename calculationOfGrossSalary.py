# Write a PYTHON program to input basic salary of an employee and calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%


basicSalary = float(input('Enter Your Basic Salary: '))

if basicSalary >= 0 and basicSalary <= 10000 :
    HRA = basicSalary/100*20
    DA = basicSalary/100*80
    grossSalary = basicSalary + HRA + DA
    print(grossSalary)
elif basicSalary >= 10001 and basicSalary <= 20000 :
    HRA = basicSalary/100*25
    DA = basicSalary/100*90
    grossSalary = basicSalary + HRA + DA
    print(grossSalary)
elif basicSalary > 20000 :
    HRA = basicSalary/100*30
    DA = basicSalary/100*95
    grossSalary = basicSalary + HRA + DA
    print(grossSalary)

    # SOLVED