fuel_type = input()
fuel_amount = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

if fuel_type == "Gas":
    if club_card == "Yes":
        if 20 <= fuel_amount <= 25:
            fuel_price = fuel_amount * (gas_price - 0.08)
            fuel_price = fuel_price - (fuel_price * 0.08)
            print(f"{fuel_price:.2f} lv.")
        elif fuel_amount < 20:
            fuel_price = fuel_amount * (gas_price - 0.08)
            print(f"{fuel_price:.2f} lv.")
        else:
            fuel_price = fuel_amount * (gas_price - 0.08)
            fuel_price = fuel_price - (fuel_price * 0.1)
            print(f"{fuel_price:.2f} lv.")
    elif club_card == "No":
        if 20 <= fuel_amount <= 25:
            fuel_price = fuel_amount * gas_price
            fuel_price = fuel_price - (fuel_price * 0.08)
            print(f"{fuel_price:.2f} lv.")
        elif fuel_amount < 20:
            fuel_price = fuel_amount * gas_price
            print(f"{fuel_price:.2f} lv.")
        else:
            fuel_price = fuel_amount * gas_price
            fuel_price = fuel_price - (fuel_price * 0.1)
            print(f"{fuel_price:.2f} lv.")
elif fuel_type == "Gasoline":
    if club_card == "Yes":
        if 20 <= fuel_amount <= 25:
            fuel_price = fuel_amount * (gasoline_price - 0.18)
            fuel_price = fuel_price - (fuel_price * 0.08)
            print(f"{fuel_price:.2f} lv.")
        elif fuel_amount < 20:
            fuel_price = fuel_amount * (gasoline_price - 0.18)
            print(f"{fuel_price:.2f} lv.")
        else:
            fuel_price = fuel_amount * (gasoline_price - 0.18)
            fuel_price = fuel_price - (fuel_price * 0.1)
            print(f"{fuel_price:.2f} lv.")
    elif club_card == "No":
        if 20 <= fuel_amount <= 25:
            fuel_price = fuel_amount * gasoline_price
            fuel_price = fuel_price - (fuel_price * 0.08)
            print(f"{fuel_price:.2f} lv.")
        elif fuel_amount < 20:
            fuel_price = fuel_amount * gasoline_price
            print(f"{fuel_price:.2f} lv.")
        else:
            fuel_price = fuel_amount * gasoline_price
            fuel_price = fuel_price - (fuel_price * 0.1)
            print(f"{fuel_price:.2f} lv.")
elif fuel_type == "Diesel":
    if club_card == "Yes":
        if 20 <= fuel_amount <= 25:
            fuel_price = fuel_amount * (diesel_price - 0.12)
            fuel_price = fuel_price - (fuel_price * 0.08)
            print(f"{fuel_price:.2f} lv.")
        elif fuel_amount < 20:
            fuel_price = fuel_amount * (diesel_price - 0.12)
            print(f"{fuel_price:.2f} lv.")
        else:
            fuel_price = fuel_amount * (diesel_price - 0.12)
            fuel_price = fuel_price - (fuel_price * 0.1)
            print(f"{fuel_price:.2f} lv.")
    elif club_card == "No":
        if 20 <= fuel_amount <= 25:
            fuel_price = fuel_amount * diesel_price
            fuel_price = fuel_price - (fuel_price * 0.08)
            print(f"{fuel_price:.2f} lv.")
        elif fuel_amount < 20:
            fuel_price = fuel_amount * diesel_price
            print(f"{fuel_price:.2f} lv.")
        else:
            fuel_price = fuel_amount * diesel_price
            fuel_price = fuel_price - (fuel_price * 0.1)
            print(f"{fuel_price:.2f} lv.")

