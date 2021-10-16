budget = int(input())
season = input()
fisherman = int(input())

rent_price = 0
if season == "Spring":
    rent_price = 3000
elif season == "Summer" or season == "Autumn":
    rent_price = 4200
elif season == "Winter":
    rent_price = 2600

if fisherman <= 6:
    rent_price = rent_price - (rent_price * 0.1)
elif 7 <= fisherman <= 11:
    rent_price = rent_price - (rent_price * 0.15)
elif fisherman >= 12:
    rent_price = rent_price - (rent_price * 0.25)

if fisherman % 2 == 0 and season == "Spring":
    rent_price = rent_price - (rent_price * 0.05)
elif fisherman % 2 == 0 and season == "Summer":
    rent_price = rent_price - (rent_price * 0.05)
elif fisherman % 2 == 0 and season == "Winter":
    rent_price = rent_price - (rent_price * 0.05)
else:
    rent_price = rent_price

if budget >= rent_price:
    extra_money = budget - rent_price
    print(f"Yes! You have {extra_money:.2f} leva left.")
else:
    lack = rent_price - budget
    print(f"Not enough money! You need {lack:.2f} leva.")