count_magnolii = int(input())
count_zumb = int(input())
count_roses = int(input())
count_cactus = int(input())
price_of_gift = float(input())
import math

earn_money = (count_magnolii * 3.25) + (count_zumb * 4) + (count_roses * 3.5) + (count_cactus * 8)
clear_earn_money = earn_money - (earn_money * 0.05)
if clear_earn_money >= price_of_gift:
    extra = clear_earn_money - price_of_gift
    print(f"She is left with {math.floor(extra)} leva.")
else:
    lack = price_of_gift - clear_earn_money
    print(f"She will have to borrow {math.ceil(lack)} leva.")