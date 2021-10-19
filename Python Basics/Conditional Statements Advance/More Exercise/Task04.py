budget = float(input())
season = input()

class_car = ""
type_car = ""
price_car = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.35
    else:
        type_car = "Jeep"
        price_car = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.45
    else:
        type_car = "Jeep"
        price_car = budget * 0.8
elif budget > 500:
    class_car = "Luxury class"
    type_car = "Jeep"
    price_car = budget * 0.9

print(class_car)
print(f"{type_car} - {price_car:.2f}")
