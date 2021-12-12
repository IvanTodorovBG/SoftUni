n = int(input()) #lost fights
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

lost_fights_count = 0
helmet_brakes = 0
sword_brakes = 0
shield_brakes = 0
armor_brakes = 0
total_shield_brakes = 0

for x in range(n):
    lost_fights_count += 1

    if lost_fights_count % 2 == 0:
        helmet_brakes += 1
    if lost_fights_count % 3 == 0:
        sword_brakes += 1
        if lost_fights_count % 2 == 0:
            shield_brakes += 1
            total_shield_brakes += 1
    if shield_brakes % 2 == 0 and shield_brakes != 0:
        armor_brakes += 1
        shield_brakes = 0

expenses = (helmet_brakes * helmet_price) + (sword_brakes * sword_price) \
    + (total_shield_brakes * shield_price) + (armor_brakes * armor_price)

print(f"Gladiator expenses: {expenses:.2f} aureus")
