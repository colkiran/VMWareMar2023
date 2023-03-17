
class Player:           # pascal casing

    def __init__(self):
        print("Player initialized......")

    def get_runs(self):
        print("runs scored.......")

sachin = Player()
sourav = Player()
sachin.__init__()

print("-"* 40)
sourav.get_runs()
sachin.get_runs()
