
class Player:

    team = "India"          # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_detials(self):
        print(f"Name is :{self.name}\nAge is :{self.age}")

ply1 = Player("Dravid", 32)
ply1.get_detials()

print("-" * 40)
ply2 = Player("Kumble", 31)
ply2.get_detials()

print("-" * 40)
print("Player :", Player.team)
print("ply1   :", ply1.team)
print("ply2   :", ply2.team)

print("-" * 40)
Player.team = "RCB"
print("Player :", Player.team)
print("ply1   :", ply1.team)
print("ply2   :", ply2.team)

print("-" * 40)
ply1.team = "RR"
print("ply1   :", ply1.team)
print("Player :", Player.team)
print("ply2   :", ply2.team)

print("-" * 40)
print(ply1.__dict__)
print(ply2.__dict__)

print("-" * 40)
print(Player.__dict__)

