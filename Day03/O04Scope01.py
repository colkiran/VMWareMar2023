
glbX = 100

def fun(y):         # y - local variable
    global glbX     # do not assign a value
    print(f"y :{y}")
    glbX = 500
    print(f"glbX Inside :{glbX}")
    print (locals())


print(f"Before :{glbX}")
fun(25)
print(f"After :{glbX}")

# print(globals())
