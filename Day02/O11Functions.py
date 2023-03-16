
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.........")

# city is called a default argument and gname is called as non default arg
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.........")


greet()

print("-" * 40)

greetGst("Sachin")
greetGst("Rahul")

print("-" * 40)

greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
# functions with simple args

def myProdcuct(x, y):
    return x * y

print("%i * %i = %i" % (10, 20, myProdcuct(10, 20)))

# variable number of args - list, dict
print("-" * 40)
def productAll(*numbers):           # *numbers can accept more than one val
    print(numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = productAll(1, 2, 3, 4, 5)
print(f'res :{res}')

# dictionary

def extract_details(**details):    # **details will accept args in the form of dictionary
    print(details)
    for k, v in details.items():
        print(k, "=>", v)


extract_details(name="Kenedy", age=21, dept='IT', desig='SE')

print("-" * 40)
# function can return values

def mul_me(x):
    y = x * x
    return y

print(mul_me(10))
a = mul_me(2)
b = mul_me(3)
c = a + b
print(c)

# python supports recursive calls
# find the factorial of a number  using recursiive calls
print("-" * 40)

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

num = 5
print(f"The factorial of {num} is :{fact(num)}")

print("-" * 40)

def basicArithmetic(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = basicArithmetic(20, 8)
print(f"res :{res}")

print("-" * 40)
# doc strings
def fun():
    # This is a comment
    "This is document-1"
    "This is document-2"

    print("Hello World")

fun()
print(f"doc_string :{fun.__doc__}")

print("-" * 40)

def fun1(x, y):
    """
        funtion - fun1
        ---------------
        function fun1 takes two arguments
        1. if both the arguments are numbers then it returns the sum of it
        2. if both the arguments are strings then it concatenates
        3. if one argument is integer and other is a string then it throws an error
    """

    return x + y

print(fun1(10, 20))
print(fun1("hello ", "world"))

print("-" * 40)

help(fun1)
