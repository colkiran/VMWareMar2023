
print("Numbers :", list(range(1, 11)))
print("Squares :", [x ** 2 for x in range(1, 11)])

print("-" * 40)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")
words = [word for word in sentence.split()]
print(f"words :{words}")

print("-" * 40)
fruits = [
    ('apple', 290),
    ('orange', 75),
    ('grapes', 145),
    ('banana', 65),
    ('gauva', 120),
    ('watermelon', 180),
    ('pears', 235),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")
print("-" * 40)

print(['fruit' for fruit in fruits])
print("-" * 40)

prices = [fruit for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

prices = [fruit[1] * 0.9 for fruit in fruits]       # disc 10%
print(f"prices :{prices}")
print("-" * 40)

prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")
print("-" * 40)

prices = [(fruit[0],"=>", fruit[1], fruit[1] * 0.9, fruit[1] * 0.75)
          for fruit in fruits if fruit[1] > 100]
print(f"prices :{prices}")
