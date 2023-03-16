
"""
sort    - sorts the original list

sorted  - returns a copy of sorted list

"""

print("sort".center(40, "-"))

l1= [10, 6, 8, 2, 9, 1, 4, 7, 3, 5]
print(f"l1 :{l1}")

res1 = sorted(l1)
print(f"Ascending order :{res1}")

res2 = sorted(l1, reverse=True)
print(f"Descending order :{res2}")

print("-" * 40)

l1= [10, 'zebra', 6, 'apple', 8, 'yellow', 2, 'blue', 9, 'white', 1, 'green', 4, 'violet', 7, 'pink', 3, 'red', 5, 'cat', 'dog', 'egg', 182, 1234, 26, 230, 2190]
print(f"l1 :{l1}")

print("-" * 40)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 40)
res1 = res[0:res.index('zebra')+1] + sorted(res[res.index(1):res.index(9)])
# res2 = sorted(res[res.index(1):res.index(9)])

print(f"res1 :{res1}")

print("-" * 40)

cities = ['kanyakumari', 'bangalore', 'ooty', 'delhi', 'thiruvananthapuram', 'mumbai', 'hyderabad', 'vishakapatnam', 'chennai', 'kolkota']
print(f"cities :{cities}")

print("-" * 40)
asc = sorted(cities, key=len)
desc = sorted(cities, key=len, reverse=True)

print(f"ascending :{asc}")
print("-" * 40)
print(f"descending :{desc}")

print("-" * 40)

months = ['dec', 'aug', 'oct', 'feb', 'nov', 'apr', 'sep', 'jan', 'may', 'jun', 'mar', 'jul']

