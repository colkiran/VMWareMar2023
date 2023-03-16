
print("copy".center(40, "-"))

emp1 = {'name': 'Micheal', 'age': 39, 'desig': 'MGR', 'dept': "MKT", 'salary': 90000}
print(f"emp1 before :{emp1}")
emp2 = emp1         # shallow copy

print(f"emp2 before : {emp2}")

print("-" * 40)
emp2['gender'] = "male"
emp2['team']  = "India"

print(f"emp2 :{emp2}")
print(f"emp1 :{emp1}")

print("-" * 40)
print("-" * 40)

ply1 = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': 98, 'oppn': 'NZL'}
print(f"ply1 before :{ply1}")

ply2 = ply1.copy()

print(f"ply2 before :{ply2}")
print("-" * 40)

ply2['venue'] = 'Auckland'
ply2['gender'] = 'Male'

print(f"ply2 after :{ply2}")
print(f"ply1 after :{ply1}")

print("-" * 40)
print("-" * 40)

ply3 = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': {'odi1':98, 'odi2': 15, 'odi3': 120},  'oppn': 'NZL'}
print(f"ply3 :{ply3}")

ply4 = ply3.copy()

print(f"ply4 before :{ply4}")

print("-" * 40)
ply4['runs']['odi4'] = 156
ply4['runs']['odi5'] = 86

print(f"ply4 after :{ply4}")
print(f'ply3 after :{ply3}')


print("-" * 40)
print("-" * 40)

ply3 = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': {'odi1':98, 'odi2': 15, 'odi3': 120},  'oppn': 'NZL'}
print(f"ply3 :{ply3}")
from copy import deepcopy

ply4 = deepcopy(ply3)

print(f"ply4 before :{ply4}")

print("-" * 40)
ply4['runs']['odi4'] = 156
ply4['runs']['odi5'] = 86

print(f"ply4 after :{ply4}")
print(f'ply3 after :{ply3}')