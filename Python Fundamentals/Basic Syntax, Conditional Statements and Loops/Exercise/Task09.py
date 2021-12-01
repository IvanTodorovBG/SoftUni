budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_liter_price = flour_price + (flour_price * 0.25)
colored_eggs_count = 0
bread_count = 0
price_for_one_bread = eggs_price + flour_price + (milk_liter_price / 4)

while True:
    if price_for_one_bread > budget:
        break
    bread_count += 1
    colored_eggs_count += 3
    if bread_count % 3 == 0:
        colored_eggs_count -= (bread_count - 2)
    budget -= price_for_one_bread

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
