decoration_quantity = int(input())
days_left_until_xmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

days_count = 0
budget = 0
spirit = 0

while True:
    days_count += 1
    days_left_until_xmas -= 1
    if days_count % 11 == 0:
        decoration_quantity += 2
    if days_count % 2 == 0:
        budget += ornament_set_price * decoration_quantity
        spirit += 5
    if days_count % 3 == 0:
        budget += (tree_skirt_price * decoration_quantity) + (tree_garlands_price * decoration_quantity)
        spirit += 13
    if days_count % 5 == 0:
        budget += tree_lights_price * decoration_quantity
        spirit += 17
        if days_count % 3 == 0:
            spirit += 30
    if days_count % 10 == 0:
        budget += (tree_skirt_price + tree_garlands_price + tree_lights_price)
        spirit -= 20
        if days_left_until_xmas == 0:
            spirit -= 30
            break
    if days_left_until_xmas == 0:
        break
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")


