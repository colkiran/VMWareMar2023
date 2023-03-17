

class Employee:

    def __init__(self, name):
        self.__name = name          # private variable
        self.tech = ['C', 'C++', 'Dotnet', 'Angular', 'React']

    def __str__(self):
        return self.__name + " " + ",".join([str(v) for v in self.tech])

emp1 = Employee("Peter")
print(emp1)

print("-" * 40)
# print(emp1.__name)
print(emp1.__dict__)
emp1._Employee__name = "John"

print(emp1.__dict__)
print(emp1)
