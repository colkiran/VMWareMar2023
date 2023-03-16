
print("fromkeys".center(40, "-"))
# used to convert a list into a dictionary

cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd']
print(f"cities :{cities}")
print(type(cities))

print("-" * 40)
res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities,23)
print(f"res2 :{res2}")

print("pop".center(40, "-"))
player = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': 98, 'oppn': 'NZL', 'team': 'India', 'venue': 'Auckland'}
print(f"player :{player}")

print("-" * 40)

res = player.pop('age')
print(f"res :{res}")

res = player.pop('team')
print(f"res :{res}")

# res = player.pop("abc")
# print(f"res :{res}")

print(f"player: {player}")

print("popitem".center(40, "-"))
player = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': 98, 'oppn': 'NZL', 'team': 'India', 'venue': 'Auckland'}
print(f"player :{player}")

print("-" * 40)

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")

print("update".center(40, "-"))

emp1 = {'name': 'Micheal', 'age': 39, 'desig': 'MGR', 'dept': "MKT"}
emp2 = {'name': 'Tina', 'age': 32, 'desig': 'SE', 'salary': 75000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)

emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(40, "-"))
emp1 = {'name': 'Micheal', 'age': 39, 'desig': 'MGR', 'dept': "MKT"}

print(f"emp1 before :{emp1}")

emp1.clear()

print(f"emp1 after :{emp1}")
