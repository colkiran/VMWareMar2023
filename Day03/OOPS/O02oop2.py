class Animal:
    def __init__(self):
        print("Animal Ctor")
        self.age = 1

    def eat(self):
        print("Animal Eat")


class Bird(Animal):
    def __init__(self):  # overriding animal ctor
        super().__init__()
        self.size = "1k"
        print("Bird Ctor")

    def fly(self):
        print("Birds Fly")


cuckoo = Bird()
print(cuckoo.__dict__)
print(cuckoo.age)
print(cuckoo.size)
