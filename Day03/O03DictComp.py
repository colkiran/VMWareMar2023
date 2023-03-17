
l = list(range(1, 11))
print(f"l :{l}")

print("-" * 40)
squares = {x: x ** 2 for x in l}
print(f"squares :{squares}")

print("-" * 40)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 40)
word_len = {word: len(word) for word in sentence.split()}
print(f"word length :{word_len}")

print("-" * 40)
word_len = {word: len(word) for word in sentence.split() if word != 'the'}
print(f"word length :{word_len}")

print("-" * 40)
players = {
    'sachin': [285, 345, 429, 400, 380],
    'sourav': [320, 375, 280, 150, 360],
    'rahul': [285, 250, 190, 325, 365],
    'sehwag': [390, 410, 360, 445, 390],
    'laxman': [180, 265, 160, 320, 300],
    'yuvraj': [125, 195, 289, 235, 175]
}

print(f"players :{players}")

print("-" * 40)
print(f"sachin :{players['sachin']}")
print(f"sachin :{sum(players['sachin'])}")

print("-" * 40)
scores = [score for score in players]
print(f"scores :{scores}")

print("-" * 40)
scores = {k: v for k,v in players.items()}
print(f"scores :{scores}")

print("-" * 40)
scores = {k: sum(v) for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 40)
scores = {k: (lambda score: sum(score) / len(score))(v) for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 40)
def average(scr):
    return sum(scr) / len(scr)

scores = {k: average(v) for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 40)
res = {x: (lambda par: "Mr." + par) ("Sachin {}".format(x))
        for x in range(1, 6)}
print(res)

print("-" * 40)
scores = [score for score in players.values()]
print(f"scores :{scores}")

# convert this into a one dimension array
print("-" * 40)
scores = [scr for score in players.values() for scr in score]
print(f"scoress :{scores}")

print("-" * 40)
scores = [scr for score in players.values() for scr in score if scr >= 200]
print(f"scores :{scores}")

print("-" * 40)
scores = {name: [scr for scr in score if scr >= 200] for name, score in players.items()}
print(f"scores :{scores}")
