from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self):
        print("Account")

    @abstractmethod
    def getBalance(self):
        pass


class Savings(Account):
    def getBalance(self):
        print("get savings ba ")


class Current(Account):
    def transaction(self):
        print("Current Transaction")

    def getBalance(self):
        print("get current balance ")


sa = Savings()
curr = Current()

curr.transaction()
curr.getBalance()
sa.getBalance()
