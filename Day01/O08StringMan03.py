
print("split".center(40, "-"))
# split converts a string into a list
st = "the quick brown fox jumps over the lazy dog"
res = st.split()
print(f"res :{res}")

print("Join".center(40, "-"))
# converts a list into a string
print(f"res :{res}")

res1 = " ".join(res)
print(f"res1 :{res1}")

print("\n", "=" * 40,  "\n")
# formatting
# emulate c style, printf
format = "Welcome %s, what a %s player"
print(format)
values = ('Sachin', 'class')            # tuple
print(values)

print(format, values)
print(format % values)

print("Welcome %s, what a %s player" % ('Sachin', 'class'))

print("Welcome %s with a rating of %d, what a %s player" % ('Sachin', 4.8, 'class'))
print("Welcome %s with a rating of %.3f, what a %s player" % ('Sachin', 4.8, 'class'))
print("Welcome %s with a rating of %.3f, what a %s player" % ('Sachin', 4.892156, 'class'))

print("Interpolation".center(40, "-"))
from math import pi, e
print(f"The value of PI={pi} and Eulers constant={e}")

print("Python String format".center(40, "-"))
print("Welcome {}, what a {} player".format("Sachin", "class"))
print("Welcome {pname}, what a {adj} player".format(pname="Sachin", adj="class"))
print("Welcome {pname} with a rating of {rating}, what a {adj} player".format(pname="Sachin", rating=4.8,  adj="class"))

print("Welcome {0} with a rating of {1}, what a {2} player".format("Sachin", 4.8, "class"))
print("Welcome {1} with a rating of {3}, what a {0} player for {2}".format("Sachin", 4.8, "class", "India"))
print("Welcome {1} with a rating of {3}, what a {0} player for {2}".format("class", "Sachin",   "India",4.8))

print("Welcome {0} with a rating of {1}, what a {adj} player for {ctry}".format("Sachin", 4.8, adj = "class", ctry="India"))

print("Conversion".center(40, "-"))
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!a} {val!r}".format(val="A"))            # string, ascii, rawstring

print("{val} {val} {val}".format(val=36))
print("{val} {val:f} {val:b}".format(val=36))
print("{val:10} {val:f} {val:b}".format(val=36))
print("{val:5} {val:f} {val:b}".format(val=36))
print("{val:5} {val:f} {val:b}".format(val=3622675688676))

print("Alignment".center(40, "-"))
print("{num:15}Tendulkar".format(num="Sachin"))
print("{num:15}Tendulkar".format(num=45))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))
print("{pi:10}".format(pi=pi))
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))

print("{pi:010.3}".format(pi=pi))
print("-" * 40)

print("{val:>15} Tendulkar".format(val="Sachin"))       # right aligned
print("{val:^15} Tendulkar".format(val="Sachin"))       # center aligned
print("{val:<15} Tendulkar".format(val="Sachin"))       # Left aligned

print("-" * 40)
print("{val:->15} Tendulkar".format(val="Sachin"))       # right aligned
print("{val:*^15} Tendulkar".format(val="Sachin"))       # center aligned
print("{val:#<15} Tendulkar".format(val="Sachin"))       # Left aligned

print("-" * 40)
print("Alignment".center(40, "-"))
print("{txt:-^40}".format(txt="Alignment"))

