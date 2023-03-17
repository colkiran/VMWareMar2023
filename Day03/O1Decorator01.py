

def outerFun(fnc):

    def innerFun(a, b):
        if b > a:
            a, b = b, a
        print(fnc(a, b))
        print("-" * 40)

    return innerFun

@outerFun
def diff(x, y):
    return x - y

diff(10, 4)
diff(10, 20)

