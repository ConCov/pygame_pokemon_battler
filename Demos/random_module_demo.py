import random

hit_points = random.randint(1, 3)

print(hit_points)

if hit_points == 1:
    print("-1 hit point change")
elif hit_points == 2:
    print("0 hit point change")
else:
    print("+1 hit point change")
