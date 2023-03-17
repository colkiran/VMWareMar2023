class Animal:
    def eat(self):
        print("Animal Eat")


class Bird(Animal):
    def fly(self):
        print("Birds Fly")


class Chicken(Bird):
    pass


chick = Chicken()

chick.eat()
chick.fly()
