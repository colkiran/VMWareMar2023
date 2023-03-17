
def outerfun(fnc):
    def innerfun(a,b):
        if b>a:
            a,b = b,a
        print(fnc(a,b))
        print("-"*40)

    return innerfun

@outerfun
def diff(x,y):
    return x-y

diff(10,4)
