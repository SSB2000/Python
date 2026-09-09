# Class Variable: Shared by all instance

class Employee:

    # class variable
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'

        Employee.num_of_employees += 1

    def apply_raise(self):
        self.pay = float(self.pay * Employee.raise_amount)


emp_01 = Employee('Shubham', 'Bohra', 10)

print(emp_01.pay)
emp_01.apply_raise()
print(emp_01.pay)
print(Employee.num_of_employees)


# instance namespace
print(emp_01.__dict__)

# Output
'''
10
10.4
1
{'firstName': 'Shubham', 'lastName': 'Bohra', 'pay': 10.4, 'email': 'Shubham.Bohra@company.com'}
'''


# Ref: Corey Schafer's Python OOP Tutorial 2: Class Variables: https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2
