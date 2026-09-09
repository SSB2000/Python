# Dataclasses: Intended to store data, no need to write __init__, __repr__, __eq__ etc


from dataclasses import dataclass

'''
class Employee:

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
'''        
# is equal to 

@dataclass(order=True)
class Employee:
    firstName: str
    lastName: str
    pay: int = 0 # Default values

emp_01 = Employee('Shubham', 'Bohra', 10)
print(emp_01)

emp_02 = Employee('Raj', 'Singh', 20)
print(emp_01 < emp_02)

