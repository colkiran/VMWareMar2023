
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'name': 'Jack', 'age': 32, 'dept': 'finance', 'desig': 'TL', 'sal': 65000}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'Sachin'), ('age', 30), ('runs', 104), ('oppn', 'Aus')])
print(f"d3 : {d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='Rahul', age=32, runs=85, oppn='SA')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
# create
player = {'name': 'sachin', 'age':34, 'runs': 98, 'oppn': 'NZL'}
print(f"player :{player}")

print("-" * 40)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 40)
# iterate
for x in player:
    print(x, "=>", player[x])

print("-" * 40)
# update - addnew, modify
player['name']  = "Sachin Tendulkar"
player['age'] = '32'
player['team'] = "India"
player['venue'] = 'Auckland'

print(f"player :{player}")

print("-" * 40)
# delete

del player['oppn']
del player['venue']
del player['runs']

print(f"player :{player}")

# print("-" * 40)
# print(dir(d1))

print("keys".center(40, "-"))

player = {'name': 'Sachin Tendulkar', 'age': '32', 'runs': 98, 'oppn': 'NZL', 'team': 'India', 'venue': 'Auckland'}
print(f"player :{player}")

k = player.keys()
print(f"k :{k}")
print("-" * 40)

for k in player.keys():
    print(k + " => " + str(player[k]))


