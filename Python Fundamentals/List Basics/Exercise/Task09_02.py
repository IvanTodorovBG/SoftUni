items = input().split("|")
budget = int(input())

spend_money = []
profit = 0
new_prices = []

for item in items:

    order = item.split("->")[0]
    price = float(item.split("->")[1])

    if order == "Clothes":
        if price <= 50:
            if budget >= price:
                budget -= price
                spend_money.append(price)

    elif order == "Shoes":
        if price <= 35:
            if budget >= price:
                budget -= price
                spend_money.append(price)

    elif order == "Accessories":
        if price <= 20.5:
            if budget >= price:
                budget -= price
                spend_money.append(price)

for current_spend_money in spend_money:
    new_prices.append(current_spend_money + (current_spend_money * 0.4))

new_budget = sum(new_prices) + budget
profit = sum(new_prices) - sum(spend_money)
new_prices = " ".join(str(f"{num:.2f}") for num in new_prices)

print(f"{new_prices}")
print(f"Profit: {profit:.2f}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")


