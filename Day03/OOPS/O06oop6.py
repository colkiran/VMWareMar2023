from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):
    def doJob(self):
        print("Manager Job")


class Developer(ABC):
    def doJob(self):
        print("Developer Job")


def BankFun(emp):  # polymorphism
    print("BankjobStarted".center(40, '_'))
    emp.doJob()
    print("BankjobCompleted".center(40, '_'))
    print('_' * 40)


manoj = Manager()
devi = Developer()

BankFun(manoj)
BankFun(devi)


def BankFunJobs(emps):  # polymorphism
    print("Started".center(40, '_'))
    for emp in emps:
        emp.doJob()
    print("Completed".center(40, '_'))
    print('_' * 40)


BankFunJobs([manoj, devi])
