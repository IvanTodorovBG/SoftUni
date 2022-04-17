materials = [int(x) for x in input().split(" ")]
magic = [int(x) for x in input().split(" ")]
gifts = []

for current_index in range(min(len(materials), len(magic))):

    mix_mat_and_magic = materials[-1] + magic[0]
    if mix_mat_and_magic < 100:
        if mix_mat_and_magic % 2 == 0:
            mix_mat_and_magic = (materials[-1] * 2) + (magic[0] * 3)
        else:
            mix_mat_and_magic = (materials[-1] * 2) + (magic[0] * 2)

    elif mix_mat_and_magic > 499:
        mix_mat_and_magic /= 2

    if 100 <= mix_mat_and_magic <= 199:
        gifts.append("Gemstone")
        materials.pop(-1)
        magic.pop(0)

    elif 200 <= mix_mat_and_magic <= 299:
        gifts.append("Porcelain Sculpture")
        materials.pop(-1)
        magic.pop(0)

    elif 300 <= mix_mat_and_magic <= 399:
        gifts.append("Gold")
        materials.pop(-1)
        magic.pop(0)

    elif 400 <= mix_mat_and_magic <= 499:
        gifts.append("Diamond Jewellery")
        materials.pop(-1)
        magic.pop(0)

    else:
        materials.pop(-1)
        magic.pop(0)

if "Gemstone" in gifts and "Porcelain Sculpture" in gifts or "Gold" in gifts and "Diamond Jewellery" in gifts:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

if gifts:
    items = sorted(set(gifts))
    for current_item in items:
        print(f"{current_item}: {gifts.count(current_item)}")
