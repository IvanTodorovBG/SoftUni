def orders(product, quantity):
    total_price = None
    if product == "coffee":
        total_price = 1.5 * quantity
    elif product == "water":
        total_price = 1.00 * quantity
    elif product == "coke":
        total_price = 1.40 * quantity
    elif product == "snacks":
        total_price = 2.00 * quantity
    return total_price


p = input()
q = float(input())

print(f"{orders(p, q):.2f}")