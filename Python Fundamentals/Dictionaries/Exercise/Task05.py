farming = input()
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
legendary_item = ""
won = False
while True:
    farming = farming.lower().split(" ")
    searched_materials = ("shards", "fragments", "motes")

    for current_index in range(0, len(farming), 2):
        current_material = farming[current_index + 1]
        current_value = int(farming[current_index])

        # collect only searched materials
        if current_material in searched_materials:
            if current_material not in key_materials:
                key_materials[current_material] = current_value
            else:
                key_materials[current_material] += current_value

            # check if value >= 250
            if key_materials[current_material] >= 250:
                if current_material == "motes":
                    key_materials[current_material] -= 250
                    legendary_item = "Dragonwrath"
                elif current_material == "fragments":
                    key_materials[current_material] -= 250
                    legendary_item = "Valanyr"
                elif current_material == "shards":
                    key_materials[current_material] -= 250
                    legendary_item = "Shadowmourne"
                print(f"{legendary_item} obtained!")
                won = True
                break
            if won:
                break

        # collect only junk materials
        else:
            if current_material not in junk_materials:
                junk_materials[current_material] = current_value
            else:
                junk_materials[current_material] += current_value
    if won:
        break
    else:
        farming = input()

key_materials_sorted = dict(sorted(key_materials.items(), key= lambda x: (-x[1], x[0])))
junk_materials_sorted = dict(sorted(junk_materials.items(), key= lambda x: x[0]))

for k, v in key_materials_sorted.items():
    print(f"{k}: {v}")
for k, v in junk_materials_sorted.items():
    print(f"{k}: {v}")