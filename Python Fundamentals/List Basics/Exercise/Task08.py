command = input().split("#")
water = int(input())
command = ", ".join(command)
fire = command.split(" = ")
fire = ", ".join(fire)
fire_list = fire.split(", ")

cells = []
effort = 0
total_fire = 0

for index, item in enumerate(fire_list):

    if item == "High":
        fire = int(fire_list[index + 1])
        if 81 <= fire <= 125:
            if water >= fire:
                water -= fire
                effort += fire * 0.25
                total_fire += fire
                cells.append(fire)

    if item == "Medium":
        fire = int(fire_list[index + 1])
        if 51 <= fire <= 80:
            if water >= fire:
                water -= fire
                effort += fire * 0.25
                total_fire += fire
                cells.append(fire)

    if item == "Low":
        fire = int(fire_list[index + 1])
        if 1 <= fire <= 50:
            if water >= fire:
                water -= fire
                effort += fire * 0.25
                total_fire += fire
                cells.append(fire)

print(f"Cells:")
for cell in cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
