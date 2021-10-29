n = int(input())

water_price = 20
internet_price = 15
others_price = 0
total_electricity_price = 0
total_water_price = 0
total_internet_price = 0

for i in range(1, n + 1):
    electricity_price = float(input())
    total_electricity_price += electricity_price
    total_water_price += water_price
    total_internet_price += internet_price
    others_price += (electricity_price + water_price + internet_price) + \
        ((electricity_price + water_price + internet_price) * 0.2)

average_total_price = (total_water_price + total_internet_price + total_electricity_price + others_price) / n

print(f"Electricity: {total_electricity_price:.2f} lv")
print(f"Water: {total_water_price:.2f} lv")
print(f"Internet: {total_internet_price:.2f} lv")
print(f"Other: {others_price:.2f} lv")
print(f"Average: {average_total_price:.2f} lv")