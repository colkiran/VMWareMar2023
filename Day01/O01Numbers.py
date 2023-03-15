
a = 10
b = -10

print(f"a :{a}")        # format or f string - interpolation
print(type(a))          # RTTI - Run time type identification
print(f"b :{b}")
print(type(b))

print("-" * 40)
c = 10.3
d = -10.3

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 40)

e = 2e3
f = -2e3

print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 40)

g = 10 + 3j
h = 10 - 3j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 40)

x = 2 + 3.5
print(f"x :{x}")

x = 2
y = 3.5
z = x + y

print(f"x = {type(x)}")
print(f"y = {type(y)}")
print(f"z = {type(z)}")

print("conversion".center(40, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(40, "-"))
print(11)
print(0b11)     # binary
print(0b101)    # binary
print(0o11)     # octal
print(0o101)    # octal
print(0xa)      # hexa
print(0xe)      # hexa

print("Number system conversion".center(40, "-"))
a = 100
print(f"{a} :{bin(a)}")
print(f"{a} :{oct(a)}")
print(f"{a} :{hex(a)}")
