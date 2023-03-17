class Animal:
    def __init__(self):
        self.a = 10
        print("Animal Ctor")

    def eat(self):
        print("Animal Eat")


class Person:
    def __init__(self):
        self.p = 20
        print("Person Ctor")

    def Talk(self):
        print("Person Talk ")


class Girl(Animal, Person):
    def __init__(self):
        self.g = 30
        super().__init__()
        # Animal.__init__(self)
        Person.__init__(self)
        print("Girl Ctor")


ruk = Girl()
print('_' * 40)
ruk.Talk()
ruk.eat()

print(ruk.__dict__)
print(ruk.a)
print(ruk.p)
print(ruk.g)
