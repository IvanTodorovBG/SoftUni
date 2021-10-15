kind_of_flowers = input()
count_flowers = int(input())
budget = int(input())

rose = 5
dalia = 3.8
tulip = 2.8
narcis = 3
gladiola = 2.5

total_price = 0

if kind_of_flowers == "Roses":
    if count_flowers > 80:
        total_price = (rose * count_flowers) - ((rose * count_flowers) * 0.1)
    else:
        total_price = rose * count_flowers
elif kind_of_flowers == "Dahlias":
    if count_flowers > 90:
        total_price = (dalia * count_flowers) - ((dalia * count_flowers) * 0.15)
    else:
        total_price = dalia * count_flowers
elif kind_of_flowers == "Tulips":
    if count_flowers > 80:
        total_price = (tulip * count_flowers) - ((tulip * count_flowers) * 0.15)
    else:
        total_price = tulip * count_flowers
elif kind_of_flowers == "Narcissus":
    if count_flowers < 120:
        total_price = (narcis * count_flowers) + ((narcis * count_flowers) * 0.15)
    else:
        total_price = narcis * count_flowers
elif kind_of_flowers == "Gladiolus":
    if count_flowers < 80:
        total_price = (gladiola * count_flowers) + ((gladiola * count_flowers) * 0.2)
    else:
        total_price = gladiola * count_flowers

if total_price <= budget:
    extra_money = budget - total_price
    print(f"Hey, you have a great garden with {count_flowers} {kind_of_flowers} and {extra_money:.2f} leva left.")
elif total_price > budget:
    lack = total_price - budget
    print(f"Not enough money, you need {lack:.2f} leva more.")
