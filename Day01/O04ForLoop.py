
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 21):
    # if i > 15:
    #     break               # come out of the iteration
    if i % 2 == 1:
        continue            # skip the iteration
    print(i, end=" ")
else:                       # for FOR_LOOP
    print("\nCompleted the iteration.....")


