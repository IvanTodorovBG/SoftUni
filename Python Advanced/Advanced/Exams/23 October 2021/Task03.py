def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."
    bought_types = set()
    answer = []
    for product, value in products.items():
        price = float(value[0])
        quantity = int(value[1])
        total_price = price * quantity
        if total_price <= budget:
            bought_types.add(product)
            budget -= total_price
            answer.append(f"You bought {product} for {total_price:.2f} leva.")
            if len(bought_types) == 5:
                break
    return '\n'.join(answer)


