
def funlogger(fnc):

    def helper():
        print("My info logged into the service........")
        fnc()
        print("My info logged out of the service........")

    return helper


def normalFun():
    print("I am a normal function......")

print("-" * 40)

normalFun = funlogger(normalFun)
normalFun()

print("-" * 40)

@funlogger
def BasicFun():
    print("This is a basic function........")

BasicFun()
