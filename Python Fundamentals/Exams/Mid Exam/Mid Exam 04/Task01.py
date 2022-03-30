food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

period = 30
pet_store = False

for days in range(1, period + 1):

    food -= 300
    if days % 2 == 0:
        hay = hay - (food * 0.05)
    if days % 3 == 0:
        cover -= (weight / 3)
    if food <= 0 or hay <= 0 or cover <= 0:
        pet_store = True
        break

if pet_store:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")



