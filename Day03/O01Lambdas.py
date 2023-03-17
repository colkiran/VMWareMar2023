
def add(x, y):
    return x + y

a = add

res = a(10, 20)
print(f"res :{res}")

print("-" * 40)

b = lambda x, y: x + y
res = b(25, 95)
print(f"res :{res}")

print("-" * 40)
# map, filter and reduce

l = list(range(1, 11))
print(f"l :{l}")

squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

dlr = [1, 10, 45, 250, 1500, 5000, 10000, 25000, 75000, 120000]
# convert the above dollar into indian rupees (1 dollar - 82.5 rs)

rupee = list(map(lambda x: x * 82.5, dlr))
print(f"rupee :{rupee}")

print("-" * 40)
from calendar import month_abbr
# print(list(month_abbr))

months = ['dec', 'aug', 'oct', 'feb', 'nov', 'apr', 'sep', 'jan', 'may', 'jun', 'mar', 'jul']

print(f"Unsorted Months :{months}")

res_asc = sorted(months, key = list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print(f"Sorted :{res_asc}")

print("-" * 40)
# filters
l = list(range(1, 11))

even_num = list(filter(lambda x: x % 2 == 0, l))
print(f"Even numbers :{even_num}")

l1 = [1, 2, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,]

print(f"l1 :{l1}")

print("-" * 40)

res = list(filter(lambda x: x != 1, l1))
print(f"res :{res}")

print("-" * 40)
# reduce
from functools import reduce
l = list(range(1, 11))
print(f"l :{l}")

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")

print("-" * 40)
l = [9, 5, 1, 7, 10, 8, 2, 6, 3, 4]

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")
