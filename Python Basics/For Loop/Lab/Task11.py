age = int(input())
price_washingmachine = float(input())
toy_price = int(input())
money = 0
given_money = 10
toy_count = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        money += given_money - 1
        given_money += 10
    else:
        toy_count += 1

total_money = money + (toy_price * toy_count)

if total_money >= price_washingmachine:
    diff = total_money - price_washingmachine
    print(f"Yes! {diff:.2f}")
else:
    diff = price_washingmachine - total_money
    print(f"No! {diff:.2f}")



