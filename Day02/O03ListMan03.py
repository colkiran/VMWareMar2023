

print("Count".center(40, "-"))

l1 = [1, 2, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,]

print(f"l1 :{l1}")

print("-" * 40)

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"5 :{l1.count(5)}")

print("index".center(40, "-"))

l1 = [1, 2, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,]

print(f"l1 :{l1}")

print("-" * 40)
print("3 :", l1.index(3))
print("3 :", l1.index(3, l1.index(3)+1))
print("3 :", l1.index(3, l1.index(3, l1.index(3)+1)+1))

# copy, sort, reverse

print("reverse".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

"""
reverse -   will reverse the original list
reversed - will return a copy of reversed list
"""
res = list(reversed(l1))
print(f"res :{res}")

print("-" * 40)
print(f"l1 :{l1}")

print("-" * 40)
l1.reverse()
print(f"l1 :{l1}")

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

l2 = l1             # shallow copy - copying the address along with data

print(f"l2 before :{l2}")

print("-" * 40)
l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("\n", "-" * 40,  "\n")

l3 = [2, 4, 6, 8, 10]
print(f"l3 before :{l3}")

l4 = l3.copy()          #deep copy - data gets copied

print(f"l4 before :{l4}")
print("-" * 40)

l4.extend([12, 14, 16, 18])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("\n", "-" * 40,  "\n")

l5 = [10, 20, 30, 40, [1, 2, 3, 4, 5], 50]
print(f"l5 before :{l5}")

l6 = l5.copy()

print(f"l6 before :{l6}")
print("-" * 40)

l6[4].append(6)
l6[4].append(7)
l6[4].append(8)
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("\n", "-" * 40,  "\n")

l7 = [11, 22, 33, [5, 10, 15, 20, 25], 44, 55]
print(f"l7 before :{l7}")
from copy import deepcopy

l8 = deepcopy(l7)
print(f"l8 before :{l8}")
print("-" * 40)

l8[3].append(30)
l8[3].append(35)
l8[3].append(40)
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")
