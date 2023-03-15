
print("Arithmetic Operators".center(40, "-"))
a = 10
b = 3
print(f"a :{a}")
print(f"b :{b}")
print(f"Sum    = {a + b}")
print(f"Diff   = {a - b}")
print(f"Prod   = {a * b}")
print(f"Quot   = {a / b}")
print(f"Flrdiv = {a // b}")
print(f"Exp    = {a ** b}")
print(f"Mod    = {a % b}")

print("Augmentor".center(40, "-"))
# =, +=, -=, *=, /=
a = 10
print(f"a :{a}")

a += 5
print(f"a :{a}")

a /= 3
print(f"a :{a}")

print("Comparison".center(40, "-"))
# ==, >, >=, <, <=, !=
a = 10
b = 20
print(f"a :{a}")
print(f"b :{b}")
print(f"a >= b :{a >= b}")
print(f"a == b :{a == b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical".center(40, "-"))
# and, or and not

print(f"True and True  :{True and True}")
print(f"True and False :{True and False}")

print(f"True or True  :{True or True}")
print(f"False or True :{False or True}")

print(f"not(True or True)   :{not(True or True)}")
print(f"not(True and False) :{not(True and False)}")

print("-" * 40)
print(f"ord('A') :{ord('A')}")          # integer representation of unicode char
print(f"ord('Z') :{ord('Z')}")
print(f"ord('a') :{ord('a')}")
print(f"ord('z') :{ord('z')}")

print("Ternary".center(40, "-"))
age = 18
print("Eligible" if age >= 18 else "Not Eligible")

print("Bitwise".center(40, "-"))
print(f"5 | 3 = {5 | 3}")
print(f"5 & 3 = {5 & 3}")
print(f"5 ^ 3 = {5 ^ 3}")
print(f"5 << 1 = {5 << 1}")
print(f"8 << 1 = {8 << 1}")
print(f"5 << 2 = {5 << 2}")

print(f"16 >> 1 = {16 >> 1}")
print(f"5 >> 1 = {5 >> 1}")
