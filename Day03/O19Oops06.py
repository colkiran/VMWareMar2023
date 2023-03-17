# class method

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Ctor called......")

    def get_detials(self):
        print(f"Name is :{self.name}\nAge is :{self.age}")

    @classmethod
    def CreatePlayer(cls, fn, ln, age):
        print("factory....")
        return cls(f"{fn} {ln}", age)


ply1 = Player("Virat", 34)
ply1.get_detials()

print("-" * 40)
ply2 = Player.CreatePlayer("Rohit", "Sharma", 33)
ply2.get_detials()
