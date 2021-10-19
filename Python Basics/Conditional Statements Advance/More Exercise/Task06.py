season = input()
distance = int(input())

price_per_km = 0

if distance <= 5000:
    if season in ("Spring", "Autumn"):
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.9
    else:
        price_per_km = 1.05
elif 5000 < distance <= 10000:
    if season in ("Spring", "Autumn"):
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.1
    else:
        price_per_km = 1.25
elif 10000 < distance <= 20000:
    price_per_km = 1.45

total_price = ((distance * price_per_km) * 4) * 0.9

print("%.2f" % total_price)