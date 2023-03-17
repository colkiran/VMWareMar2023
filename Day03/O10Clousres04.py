
# pip install emojis (terminal of pycharm)
# ":tiger:"

def outerFun(greet):
    def innerFun(sep):
        def innerMostFun(name):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)
        return innerMostFun
    return innerFun

KndGrt = outerFun("Namaskara")
TgrKndGrt = KndGrt("owl")
TgrKndGrt("Prabhakar")

"""
outerFun("Welcome")("---->")("Sachin")
print("-" * 40)

EngGrt = outerFun("Welcome")
EngGrtSngArw = EngGrt("----->")
EngGrtDblArw = EngGrt("======>>")

HndGrt = outerFun("Namaskar")
HndGrtSngArw = HndGrt("----->")

TmlGrt = outerFun("Vanakam")
TmlGrtSngArw = TmlGrt("----->")

EngGrtSngArw("Sachin")
HndGrtSngArw("Ravi")
TmlGrtSngArw("Ashwin")

EngGrtDblArw("Sunil")

"""