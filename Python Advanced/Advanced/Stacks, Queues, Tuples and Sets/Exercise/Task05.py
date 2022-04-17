from collections import deque
materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
doll = 0
train = 0
bear = 0
bicycle = 0
present = ["Doll", "Wooden train", "Teddy bear", "Bicycle"]
while materials and magic:

    if materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
        continue
    elif materials[-1] == 0:
        materials.pop()
        continue
    elif magic[0] == 0:
        magic.popleft()
        continue

    if materials[-1] < 0 or magic[0] < 0:
        new_product = materials[-1] + magic[0]
        materials.pop()
        magic.popleft()
        materials.append(new_product)
        continue

    if materials[-1] > 0 and magic[0] > 0:
        total_magic = materials[-1] * magic[0]

        if total_magic == 150:
            materials.pop()
            magic.popleft()
            doll += 1
        elif total_magic == 250:
            materials.pop()
            magic.popleft()
            train += 1
        elif total_magic == 300:
            materials.pop()
            magic.popleft()
            bear += 1
        elif total_magic == 400:
            materials.pop()
            magic.popleft()
            bicycle += 1
        else:
            magic.popleft()
            materials[-1] += 15

if doll and train or bear and bicycle:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

if bicycle:
    print(f"Bicycle: {bicycle}")
if doll:
    print(f"Doll: {doll}")
if bear:
    print(f"Teddy bear: {bear}")
if train:
    print(f"Wooden train: {train}")
