fires_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0

cells = []

for fire_cell in fires_cells:
    type_of_fire = fire_cell.split(" = ")[0]
    fire_level = int(fire_cell.split(" = ")[1])

    if type_of_fire == "High":
        if 81 <= fire_level <= 125:
            if water < fire_level:
                continue
            effort += fire_level * 0.25
            water -= fire_level
            total_fire += fire_level
            cells.append(fire_level)

    elif type_of_fire == "Medium":
        if 51 <= fire_level <= 80:
            if water < fire_level:
                continue
            effort += fire_level * 0.25
            water -= fire_level
            total_fire += fire_level
            cells.append(fire_level)

    elif type_of_fire == "Low":
        if 1 <= fire_level <= 50:
            if water < fire_level:
                continue
            effort += fire_level * 0.25
            water -= fire_level
            total_fire += fire_level
            cells.append(fire_level)

print("Cells:")
for cell in cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")