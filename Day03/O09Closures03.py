
def outerFun(greet):
    def innerFun(gname):
        print(greet, gname)
    return innerFun

# simple curry
EngGrt = outerFun("Welcome")
HndGrt = outerFun("Namaskar")
TmlGrt = outerFun("Vanakam")

EngGrt("Sachin")
EngGrt("Rahul")

HndGrt("Jadeja")
TmlGrt("Natraj")
