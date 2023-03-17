
def outerFun(gname):        # First Class function
                            # HOF - Higher Order Function
    def innerFun():

        print(f"Hello! {gname}")

    return innerFun


inref = outerFun('Rahul')
# after few lines of code
inref()


print("-" * 40)

outerFun("Sachin")()            # calls the inner function


# def addMe(x, y):
#     return x + y
#
# addMe(10, 20)
