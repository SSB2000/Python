# special methods __specialMethods__ (__ = dunder)

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

