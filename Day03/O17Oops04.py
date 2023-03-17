
"""
self - will have name of the object that called the method

ply1.getdetails()               => self of getdetails will have ply1 stored in it
"""

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized.......")

    def get_detials(self):
        print(f"Name is :{self.name}\nAge is :{self.age}")

ply1 = Player("Sachin", 35)
ply1.get_detials()

print("-" * 40)
ply2 = Player("Rahul", 33)
ply2.get_detials()

print("-" * 40)
print(ply1.__dict__)
print(ply2.__dict__)

ply2.runs = 60
print("-" * 40)
print(ply1.__dict__)
print(ply2.__dict__)


