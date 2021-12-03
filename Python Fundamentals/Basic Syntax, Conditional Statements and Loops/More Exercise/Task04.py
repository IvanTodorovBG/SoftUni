animals = input().split(", ")
animals.reverse()

if animals[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for index, current_animal in enumerate(animals):
        if current_animal == "wolf":
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
