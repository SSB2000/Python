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
