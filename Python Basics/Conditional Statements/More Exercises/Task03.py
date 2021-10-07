loze_area_X = int(input())
grape_per_sqmeter_Y = float(input())
enough_liter_for_wine_Z = int(input())
workers_count = int(input())

grape = loze_area_X * grape_per_sqmeter_Y
wine = (grape * 0.4) / 2.5

import math

if wine >= enough_liter_for_wine_Z:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    remaining_wine = wine - enough_liter_for_wine_Z
    wine_per_person = remaining_wine / workers_count
    print(f"{math.ceil(remaining_wine)} liters left -> {math.ceil(wine_per_person)} liters per person.")
else:
    not_enough_wine = enough_liter_for_wine_Z - wine
    print(f"It will be a tough winter! More {math.floor(not_enough_wine)} liters wine needed.")