# Basic Classes

class Employee:
    pass

emp_01 = Employee()
emp_02 = Employee()

print(emp_01)
print(emp_02)

# Output: 
'''
<__main__.Employee object at 0x000001DAA44386E0>
<__main__.Employee object at 0x000001DAA4440550>

# both emp_01 & emp_02 are instance of a class (Employee) which 
'''
#######################################################################################################

# Class variable

class Employee:
    # decorator
    def __init__(self, firstName, lastName, pay):
        # intance atributes
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'

emp_01 = Employee('Shubham', 'Bohra', 10)

print(emp_01)
print(emp_01.email)
print('{} {}'.format(emp_01.firstName, emp_01.lastName))

# Output
'''
<__main__.Employee object at 0x000001FDD11B86E0>
Shubham.Bohra@company.co
Shubham Bohra
'''
#######################################################################################################

# class method

class Employee:
    # decorator
    def __init__(self, firstName, lastName, pay):
        # intance atributes
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'

    # Method
    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

emp_01 = Employee('Shubham', 'Bohra', 10)

print(emp_01.fullName)
print(emp_01.fullName())
print(Employee.fullName(emp_01))

# Output
'''
<bound method Employee.fullName of <__main__.Employee object at 0x0000026C4A7486E0>>
Shubham Bohra
Shubham Bohra
'''