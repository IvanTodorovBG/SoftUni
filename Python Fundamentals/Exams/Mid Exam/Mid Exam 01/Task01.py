command = input()
prices = 0
taxes = 0
total_price = 0
special = False
while True:
    if command == "special" or command == "regular":
        if total_price == 0:
            print("Invalid order!")
            special = True
        if command == "special":
            total_price *= 0.9
        break

    numbers = float(command)

    if numbers < 0:
        print("Invalid price!")
    else:
        prices += numbers
        taxes += numbers * 0.2
    total_price = prices + taxes
    command = input()

if not special:
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {prices:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$
""")