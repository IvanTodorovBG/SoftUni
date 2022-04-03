n = int(input())
plant_dict = {}

for _ in range(n):
    element = input().split("<->")
    plant = element[0]
    rarity = int(element[1])
    if plant not in plant_dict:
        plant_dict[plant] = {}
        plant_dict[plant]['rating'] = []
    plant_dict[plant]['rarity'] = rarity

command = input()

while command != "Exhibition":

    command = command.split(": ")
    order = command[0]
    rating_plants = command[1]
    rating_plants = rating_plants.split(" - ")
    plant = rating_plants[0]

    if order == "Rate":
        if plant in plant_dict:
            rating = int(rating_plants[1])
            plant_dict[plant]['rating'].append(rating)
        else:
            print("error")

    elif order == "Update":
        if plant in plant_dict:
            new_rarity = int(rating_plants[1])
            plant_dict[plant]['rarity'] = new_rarity
        else:
            print("error")

    elif order == "Reset":
        if plant in plant_dict:
            plant_dict[plant]['rating'].clear()
        else:
            print("error")

    command = input()

# create avg rating

for plant in plant_dict:
    if not plant_dict[plant]['rating']:
        avg_rating = 0
    else:
        avg_rating = sum(plant_dict[plant]['rating']) / len(plant_dict[plant]['rating'])
    plant_dict[plant]['avg_rating'] = avg_rating

sorted_plant_dict = dict(sorted(plant_dict.items(), key=lambda kvp: (kvp[1]['rarity'], kvp[1]['avg_rating']), reverse=True))

print("Plants for the exhibition:")

for kvp in sorted_plant_dict.items():
    print(f"- {kvp[0]}; Rarity: {kvp[1]['rarity']}; Rating: {kvp[1]['avg_rating']:.2f}")

