
from functools import total_ordering

@total_ordering         # __eq__ with another comparison operator
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __str__(self):
        return f"Name is   :{self.name}\nSalary is :{self.salary}"

    # this works for not equal to also
    def __eq__(self, other):
        return self.salary == other.salary

    # works for less than also
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Ruben", 30000)
print(emp1)

print("-" * 40)
emp2 = Employee("Nixon", 40000)
print(emp2)

print("-" * 40)
# compares the address by default
# print(emp1 == emp2)

if emp1 != emp2:
    print("{} salary of {} is NOT equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is  equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))


print("-" * 40)
print(emp1 > emp2)

if emp1 < emp2:
    print("{} salary of {} is less than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is NOT less than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)
print(emp1 <= emp2)