

l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 4.8, 5.1, 6.9, 'seven', 'eight', 'nine', 10+2j, 11-2j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 6))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l2 = [1, 2, 3, 4.8, 5.1, 6.9, 'seven', 'eight', 'nine', 10+2j, 11-2j, True, False]
print(f"l2 :{l2}")
print(f"l2[0] :{id(l2[0])}")
print(f"l2[1] :{id(l2[1])}")
print(f"l2[2] :{id(l2[2])}")
print(f"l2[3] :{id(l2[3])}")
print(f"l2[4] :{id(l2[4])}")
print(f"l2[5] :{id(l2[5])}")

print("-" * 40)
# create
l1 = list(range(10, 101, 10))
print(f"l1 :{l1}")

print("-" * 40)
#read
print(f"l1[4]  :{l1[4]}")
print(f"l1[-1] :{l1[-1]}")

print("-" * 40)
#iteration
for i in l1:
    print(i, end=" ")
print()

print("-" * 40)
# modify - update and add a new value

l1[2] = 300
l1[7] = 800
l1[9] = 95
# l1[10] = 'hello'

print(f"l1 :{l1}")

print("-" * 40)
# del
del l1[2]
del l1[5]
del l1[7]

print(f"l1 :{l1}")

print("-" * 40)
print(dir(l1))
