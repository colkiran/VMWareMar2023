

print("values".center(40, "-"))
player = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': 98, 'oppn': 'NZL', 'team': 'India', 'venue': 'Auckland'}

print(f"player :{player}")

print("-" * 40)

v = player.values()
print(f"v :{v}")

print("items".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': 98, 'oppn': 'NZL', 'team': 'India', 'venue': 'Auckland'}

print(f"player :{player}")

print("-" * 40)

for k, v in player.items():
    print(k, "=>", v)

print("-" * 40)
emp = {
    'emp1': {'name': 'Micheal', 'age': 39, 'desig': 'MGR', 'dept': "MKT", 'salary': 90000},
    'emp2': {'name': 'Tina', 'age': 32, 'desig': 'SE', 'dept': "IT", 'salary': 75000},
    'emp3': {'name': 'Ricard', 'age': 29, 'desig': 'BDE', 'dept': "MKT", 'salary': 25000}
}

print(f"emp :{emp}")
print("-" *40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" *40)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("get".center(40, "-"))
player = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': 98}

print(f"player :{player}")
print(f"Name     :{player.get('name', 'Invalid Key, please enter a valid one')}")
print(f"Age      :{player.get('age', 'Invalid Key, please enter a valid one')}")
print(f"Opponent :{player.get('oppn', 'Invalid Key, please enter a valid one')}")

print("setdefault".center(40, "-"))
player = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': 98}
print(f"player :{player}")

player.setdefault("runs", 150)
player.setdefault("age", 34)
player.setdefault('oppn', "Australia")
player.setdefault('venue', 'Perth')

print(f"player :{player}")
