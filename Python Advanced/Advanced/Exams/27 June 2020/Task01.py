from collections import deque
bomb_effects = deque([int(num) for num in input().split(", ")])
bomb_casing = [int(num) for num in input().split(", ")]
bombs = {"cherry_bombs": 0, "datura_bombs": 0, "smoke_bombs": 0}

while True:

    if bomb_effects and bomb_casing:

        mix_bomb = bomb_effects[0] + bomb_casing[-1]

        if mix_bomb == 40:
            bombs["datura_bombs"] += 1
            bomb_effects.popleft()
            bomb_casing.pop()

        elif mix_bomb == 60:
            bombs["cherry_bombs"] += 1
            bomb_effects.popleft()
            bomb_casing.pop()

        elif mix_bomb == 120:
            bombs["smoke_bombs"] += 1
            bomb_effects.popleft()
            bomb_casing.pop()

        else:
            bomb_casing[-1] -= 5

        if bombs["datura_bombs"] >= 3 and bombs["cherry_bombs"] >= 3 and bombs["smoke_bombs"] >= 3:
            break

    else:
        break

if bombs["datura_bombs"] >= 3 and bombs["cherry_bombs"] >= 3 and bombs["smoke_bombs"] >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(num) for num in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(num) for num in bomb_casing])}")
else:
    print("Bomb Casings: empty")

ordered_bombs = dict(sorted(bombs.items(), key=lambda kvp: kvp[0]))

print(f"Cherry Bombs: {bombs['cherry_bombs']}")
print(f"Datura Bombs: {bombs['datura_bombs']}")
print(f"Smoke Decoy Bombs: {bombs['smoke_bombs']}")