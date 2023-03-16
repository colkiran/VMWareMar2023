
# add values into a list - append, extend, insert

print("{txt:-^40}".format(txt="Append"))
# can add one value into the list
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)
l1.append([10, 11, 12, 13, 14, 15])

print(f"l1 :{l1}")
print(f"l1[9] :{l1[9]}")
print(f"l1[9][2:5] :{l1[9][2:5]}")

print("extend".center(40, "-"))
l1 = [10, 20, 30, 40, 50]
print(f"l1 :{l1}")

l1.extend([60, 70, 80])
l1.extend([90, 100])

print(f"l1 :{l1}")

print("insert".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

# delete values from a list - clear, pop, remove
print("clear".center(40, "-"))
l2 = list(range(1, 11))
print(f"l2 :{l2}")

l2.clear()          # delete all the values in the list leaving a empty list

print(f"l2 :{l2}")

print("pop".center(40, "-"))
l2 = list(range(2, 11, 2))
print(f"l2 :{l2}")

# pop will return the value that was removed from the list
res = l2.pop(3)
print(f"res :{res}")

res = l2.pop(1)
print(f"res :{res}")

res = l2.pop()
print(f"res :{res}")

# res = l2.pop(3)
# print(f"res :{res}")

print(f"l2 :{l2}")

print("remove".center(40, "-"))

l1 = [1, 2, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,]

# l1.remove(3)
# l1.remove(3)
# l1.remove(3)

print(f"l1 :{l1}")

print("-" * 40)

while l1.count(1):
    l1.remove(1)

print(f"l1 :{l1}")
