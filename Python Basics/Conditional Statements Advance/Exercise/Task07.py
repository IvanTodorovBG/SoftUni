month = input()
days = int(input())

studio_price = 0
apartment_price = 0
studio_discount = 0
apartment_discount = 0

if month in ("May", "October"):
    studio_price = 50
    apartment_price = 65
elif month in ("June", "September"):
    studio_price = 75.2
    apartment_price = 68.7
elif month in ("July", "August"):
    studio_price = 76
    apartment_price = 77

if days > 14:
    apartment_discount = 0.1
    if month == "May" or month == "October":
        studio_discount = 0.3
    elif month == "June" or month == "September":
        studio_discount = 0.2
elif days > 7:
    if month == "May" or month == "October":
        studio_discount = 0.05

apartment_total_price = (apartment_price - (apartment_price * apartment_discount)) * days
studio_total_price = (studio_price - (studio_price * studio_discount)) * days

print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")