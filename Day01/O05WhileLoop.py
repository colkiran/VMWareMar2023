
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

print(f'outside :{i}')

while True:
    print(i, end=" ")
    i -= 1
    if i <= 0:
        break
