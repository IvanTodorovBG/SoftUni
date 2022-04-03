n = int(input())
plants = {}

for _ in range(n):
    element = input().split("<->")
    flower = element[0]
    rarity = int(element[1])

    if flower not in plants:
        plants[flower] = {}
        plants[flower]['rarity'] = 0
        plants[flower]['rating'] = []
    plants[flower]['rarity'] = rarity

command = input()

while command != "Exhibition":

    command = command.split(": ")
    order = command[0]
    data = command[1].split(" - ")
    flower = data[0]

    if flower in plants:

        if order == "Rate":
            rating = int(data[1])
            plants[flower]['rating'].append(rating)

        elif order == "Update":
            new_rarity = int(data[1])
            plants[flower]['rarity'] = new_rarity

        elif order == "Reset":
            plants[flower]['rating'].clear()

    else:
        print("error")

    command = input()

for kvp in plants.items():
    if kvp[1]['rating']:
        kvp[1]['avg_rating'] = sum(kvp[1]['rating']) / len(kvp[1]['rating'])
    else:
        kvp[1]['avg_rating'] = 0

sorted_plants = dict(sorted(plants.items(), key=lambda kvp: (-kvp[1]['rarity'], -kvp[1]['avg_rating'])))

print("Plants for the exhibition:")

for kvp in sorted_plants.items():
    print(f"- {kvp[0]}; Rarity: {kvp[1]['rarity']}; Rating: {kvp[1]['avg_rating']:.2f}")



