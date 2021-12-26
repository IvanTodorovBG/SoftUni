dresses = input().split("|")
budget = int(input())

sold_items = []
profit = 0

for current_dress in dresses:
    current_dress = current_dress.split("->")

    item = current_dress[0]
    price = float(current_dress[1])

    if item == "Clothes":
        if price <= 50.00:
            if budget >= price:
                budget -= price
                sold_items.append(price + (price * 0.4))
                profit += (price + (price * 0.4)) - price

    if item == "Shoes":
        if price <= 35.00:
            if budget >= price:
                budget -= price
                sold_items.append(price + (price * 0.4))
                profit += (price + (price * 0.4)) - price

    if item == "Accessories":
        if price <= 20.5:
            if budget >= price:
                budget -= price
                sold_items.append(price + (price * 0.4))
                profit += (price + (price * 0.4)) - price


print(" ".join([str(f"{i:.2f}") for i in sold_items]))
print(f"Profit: {profit:.2f}")

new_budget = budget + sum(sold_items)

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")