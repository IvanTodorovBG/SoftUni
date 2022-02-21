order = input()
products = {}
while order != "buy":

    order = order.split(" ")
    name = order[0]
    price = float(order[1])
    quantity = int(order[2])

    if name not in products:
        products[name] = {}
        products[name]["quantity"] = 0
    products[name]["price"] = price
    products[name]["quantity"] += quantity

    order = input()

for k, v in products.items():
    total = v["quantity"] * v["price"]
    print(f"{k} -> {total:.2f}")



