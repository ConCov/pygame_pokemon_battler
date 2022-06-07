import random

random_gen = random.randint(1, 3)

print(random_gen)

if random_gen == 1:
    print("-1 hit point change")
elif random_gen == 2:
    print("0 hit point change")
else:
    print("+1 hit point change")
