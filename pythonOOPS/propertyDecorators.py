# Properly Decorator (Getters & Setters)

class Employee:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    # Property Decorator (Getter)
    @property
    def email(self):
        return "{}.{}@company.com".format(self.firstName, self.lastName)

    @property
    def fullName(self):
        return "{} {}".format(self.firstName, self.lastName)


    # Property Decorator (Setter)
    @fullName.setter
    def fullName(self, newName):
        firstName, lastName = newName.split(' ')
        self.firstName = firstName
        self.lastName = lastName


    # Property Decorator (Deleter)
    @fullName.deleter
    def fullName(self):
        print('Deleted Full Name for the employee!')
        self.firstName = None
        self.lastName = None


emp_01 = Employee('Shubham', 'Bohra')

print(emp_01.firstName)
print(emp_01.email)
print(emp_01.fullName)

emp_01.fullName = 'Shivam Singh'
print(emp_01.fullName)

del emp_01.fullName
print(emp_01.fullName)

# Ref: Corey Schafer's Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters: https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
