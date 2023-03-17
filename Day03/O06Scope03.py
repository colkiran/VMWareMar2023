
# global variable cannot be used as a non local variable

def Outerfun():
    gname = "Sachin"
    print(f"Outer :{gname}")

    def InnerFun():
        nonlocal gname
        x = 100
        print("Hello World")
        # print(type(gname))
        gname = "Rahul"
        print(f"Inner :{gname}")
        print(locals())


    InnerFun()
    print(f"After :{gname}")

Outerfun()
