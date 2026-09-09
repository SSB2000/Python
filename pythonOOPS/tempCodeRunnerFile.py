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