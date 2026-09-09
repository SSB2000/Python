# class Methods

class Employee:

    raise_amount = 1

    def __init__(self, pay):
        self.pay = pay

    # Class Method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp_01 = Employee(10)

Employee.set_raise_amount(2)

print(Employee.raise_amount)
print(emp_01.raise_amount)

emp_01.set_raise_amount(3) # not used as class method should be initiated from class and not instances

print(Employee.raise_amount)
print(emp_01.raise_amount)


# Static Methods:
'''
A class method which doesn't need to reference the class itself and is standalone
'''

import datetime

class Employee:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_01 = Employee('Shubham')

day_01 = datetime.date(2016, 7, 10) # Sunday
day_02 = datetime.date(2016, 7, 11) # Monday
print(Employee.is_workday(day_01))
print(Employee.is_workday(day_02))

# Output
'''
False
True
'''

# Ref: Corey Schafer's Python OOP Tutorial 3: classmethods and staticmethods: https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3
