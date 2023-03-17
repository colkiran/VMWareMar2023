
def sum(x, y):
    print(f"adding.......{x} and {y}")
    return x + y

def diff(x, y):
    print(f"subtracting.......{x} and {y}")
    return x - y

def outerFun(fnc):

    def innerFun(a, b):
        print("Logging into the service......")
        print(fnc(a, b))
        print("-" * 40)

    return innerFun

sumlogger = outerFun(sum)
sumlogger(10, 20)

difflogger = outerFun(diff)
difflogger(20, 12)
