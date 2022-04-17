from collections import deque

materials = [int(el) for el in input().split()]
magic = deque([int(el) for el in input().split()])

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic:

    spell = materials[-1] + magic[0]

    if spell < 100:
        if spell % 2 == 0:
            spell = (materials[-1] * 2) + (magic[0] * 3)
        else:
            spell = (materials[-1] * 2) + (magic[0] * 2)

    elif spell > 499:
        spell = (materials[-1] / 2) + (magic[0] / 2)

    if 100 <= spell <= 199:
        gifts['Gemstone'] += 1
    elif 200 <= spell <= 299:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= spell <= 399:
        gifts['Gold'] += 1
    elif 400 <= spell <= 499:
        gifts['Diamond Jewellery'] += 1

    materials.pop()
    magic.popleft()

if gifts['Gemstone'] and gifts['Porcelain Sculpture'] or gifts['Gold'] and gifts['Diamond Jewellery']:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(el) for el in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(el) for el in magic])}")

sorted_dict = dict(sorted(gifts.items(), key=lambda kvpt: kvpt[0]))

for key, value in sorted_dict.items():
    if value != 0:
        print(f"{key}: {value}")
