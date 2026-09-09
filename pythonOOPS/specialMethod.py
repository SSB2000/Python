# Special/Magin methods __specialMethods__ (__ = dunder)

class Employee:

    # special method init()
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + '.' + lastName + '@company.com'

    def fullName(self):
        return self.firstName + ' ' + self.lastName

    # special method repr()
    # Intended to be used by other developer
    def __repr__(self):
        return "Employee('{}, {}')".format(self.firstName, self.lastName)

    # special method str()
    # Intended to be used by end user
    def __str__(self):
        return '{} - {}'.format(self.fullName(), self.email)


    # Other special method
    '''
    __add__()

    '''

emp_01 = Employee('Shubham', 'Bohra')

print(emp_01)
print(repr(emp_01)) # print(emp_01.__repr__())
print(str(emp_01))

# Output
'''
Shubham Bohra - Shubham.Bohra@company.com
Employee('Shubham, Bohra')
Shubham Bohra - Shubham.Bohra@company.com
'''

# Ref: Corey Schafer's Python OOP Tutorial 5: Special (Magic/Dunder) Methods: https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5
###############################################################################################################

# __eq__ & __it__

class Employee:

    def __init__(self, firstName, lastName, pay = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay

    # Equal(==)
    def __eq__(self, other):
        return self.firstName == other.firstName and self.lastName == other.lastName

    # Compare(<) lt = less than
    def __lt__(self, other):
        return self.pay < other.pay

    # Compare (>) gt = greater than
    def __gt__(self, other):
        return self.pay > other.pay

emp_01 = Employee('Shubham', 'Bohra', 10)
emp_02 = Employee('Shubham', 'Bohra', 12)

print(emp_01 == emp_02) # emp_01.__eq__(emp_02)
print(emp_01 < emp_02) # emp_01.__lt__(emp_02)
print(emp_01 > emp_02)

# Output
'''
True
True
False
'''

###############################################################################################################

# functools.total_ordering class decorator

from functools import total_ordering
@total_ordering
class Employee:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def __eq__(self, other):
        return self.name == other.name 

    def __lt__(self, other):
        return self.pay < other.pay
    
emp_01 = Employee('Shubham', 10)
emp_02 = Employee('Shubham', 20)

print(emp_01 == emp_02)
print(emp_01 < emp_02)
print(emp_01 > emp_02)