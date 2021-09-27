veg_price = float(input())
fruit_price = float(input())
veg_kg = int(input())
fruit_kg = int(input())

price = ((veg_price * veg_kg) + (fruit_price * fruit_kg)) / 1.94

print(f"{price:.2f}")