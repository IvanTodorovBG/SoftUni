money = float(input())
year_must_live = int(input())
ivan_years = 18 - 1
for years in range(1800, year_must_live + 1):
    if years % 2 == 0:
        money -= 12000
        ivan_years += 1
    if years % 2 != 0:
        ivan_years += 1
        money -= abs(12000 + (ivan_years * 50))

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    not_enough_money = abs(money)
    print(f"He will need {not_enough_money:.2f} dollars to survive.")
