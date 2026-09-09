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