'''
Recap
1. Class
2. object
3. isinstance
4. __init__
5. self
6. class attribute
7. @classmethod
8. cls
9. __str__
10.__eq__,__ne__,... ,__add__,__floor__,...
11. private variables with __
12. __dict__
13. property()  ,@property , setter
'''


class Animal:
    def __init__(self):
        print("Animal Ctor")
        self.age = 1

    def eat(self):
        print("Animal Eat")

# inheritance


class Bird(Animal):
    def fly(self):
        print("Birds Fly")


class Fish(Animal):
    def swim(self):
        print("Fishes Swim")


cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()
print('_' * 60)
dolphin = Fish()
dolphin.swim()
dolphin.eat()
print('_' * 60)


print(cuckoo.__dict__)
print(dolphin.__dict__)
print('_' * 60)


print("isinstance(cuckoo, Bird))  ", isinstance(cuckoo, Bird))
print("isinstance(cuckoo, Fish))  ", isinstance(cuckoo, Fish))
print("isinstance(cuckoo, Animal))", isinstance(cuckoo, Animal))
print("isinstance(cuckoo, object))", isinstance(cuckoo, object))
print('_' * 60)
print("isinstance(dolphin, Bird))  ", isinstance(dolphin, Bird))
print("isinstance(dolphin, Fish))  ", isinstance(dolphin, Fish))
print("isinstance(dolphin, Animal))", isinstance(dolphin, Animal))
print("isinstance(dolphin, object))", isinstance(dolphin, object))
print('_' * 60)
print("issubclass(Bird,Animal))", issubclass(Bird, Animal))
print("issubclass(Bird,object))", issubclass(Bird, object))
print("issubclass(Bird,Fish))  ", issubclass(Bird, Fish))
