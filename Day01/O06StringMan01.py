
st1 = "hello world"
print(f"st1 :{st1}")
print(type(st1))

print("-" * 40)
print(f"st1[0]  :{st1[0]}")      # strings are stored like lists(arrays)
print(f"st1[6]  :{st1[6]}")
print(f"st1[10] :{st1[10]}")

# strings are immutable
# print(f"st1[0] :{st1[0]}")
# st1[0] = "H"

print("-" * 40)
# slicing
print(f"st1[0:5]  :{st1[0:5]}")
print(f"st1[6:11] :{st1[6:11]}")
print(f"st1[0:11] :{st1[0:11]}")
print(f"st1[:11]  :{st1[:11]}")
print(f"st1[0:]   :{st1[0:]}")
print(f"st[:]     :{st1[:]}")

print("-" * 40)
# indexing in reverse order
print(f"st1[-1] :{st1[-1]}")
print(f"st1[-7] :{st1[-7]}")
print(f"st1[-11] :{st1[-11]}")

print("-" * 40)
# reverse index slicing
print(f"st1[-1:-6:-1]  :{st1[-1:-6:-1]}")
print(f"st1[-7:-12:-1] :{st1[-7:-12:-1]}")
print(f"st1[-1:-12:-1] :{st1[-1:-12:-1]}")
print(f"st1[:-12:-1]   :{st1[:-12:-1]}")
print(f"st1[-1::-1]    :{st1[-1::-1]}")
print(f"st1[::-1]      :{st1[::-1]}")

print("-" * 40)
print(dir(st1))
