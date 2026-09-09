# Inheritance

# Parent's class
class Employee:

    def __init__(self, name):
        self.name = name


# sub/child class
class Developer(Employee):

    def __init__(self, name, prog_lang):
        super().__init__(name)
        self.prog_lang = prog_lang

dev_01 = Employee('Shubham')
print(dev_01.name)

dev_02 = Developer('Shubham-Dev', 'c++')
print(dev_02.name, dev_02.prog_lang)

print(help(Developer))

# Output
'''
Shubham
Shubham-Dev c++
Help on class Developer in module __main__:                                                                                        

class Developer(Employee)
 |  Developer(name, prog_lang)
 |
 |  # sub/child class
 |
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, name, prog_lang)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

None
'''
###################################################################################################################

# Inheritance

# Parent's class
class Employee:

    def __init__(self, name):
        self.name = name


# sub/child class
class Developer(Employee):

    def __init__(self, name, prog_lang):
        super().__init__(name)
        self.prog_lang = prog_lang


class Manger(Employee):

    def __init__(self, name, employees = None):
        super().__init__(name)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            pass

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            pass

    def print_employees(self):
        print('Employee List')
        for employee in self.employees:
            print(employee.name)
        
dev_01 = Developer('Shubham', 'Python')
dev_02 = Developer('Ankit', 'Java')

manager_01 = Manger('Ashish', [dev_01, dev_02])
manager_01.print_employees()

dev_03 = Developer('Aditya', 'Apex')
manager_01.add_employee(dev_03)
manager_01.print_employees()

manager_01.remove_employee(dev_01)
manager_01.print_employees()


# Output
'''
Shubham
Ankit

Employee List
Shubham
Ankit
Aditya

Employee List
Ankit
Aditya
'''



# Ref: Python OOP Tutorial 4: Inheritance - Creating Subclasses: https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4