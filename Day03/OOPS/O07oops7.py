# duck types


class Manager:
    def doJob(self):
        print("Manager Job")


class Developer:
    def doJob(self):
        print("Developer Job")


manoj = Manager()
devi = Developer()


def BankFunJobs(emps):  # polymorphism
    print("Started".center(40, '_'))
    for emp in emps:
        emp.doJob()
    print("Completed".center(40, '_'))
    print('_' * 40)


BankFunJobs([manoj, devi])
