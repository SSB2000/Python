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