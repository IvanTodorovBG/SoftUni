days = int(input())
left_food_kg = int(input())
kg_per_day_dog = float(input())
kg_per_day_cat = float(input())
kg_per_day_turtle = float(input()) / 1000

import math

needed_food = (days * kg_per_day_dog) + (days * kg_per_day_cat) + (days * kg_per_day_turtle)

if needed_food <= left_food_kg:
    extra = left_food_kg - needed_food
    print(f"{math.floor(extra)} kilos of food left.")
else:
    lack = needed_food - left_food_kg
    print(f"{math.ceil(lack)} more kilos of food are needed.")