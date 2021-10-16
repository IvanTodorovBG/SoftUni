budget = float(input())
season = input()

destination = ""
place_to_stay = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spend_money = budget * 0.3
        place_to_stay = "Camp"
        print(f"Somewhere in {destination}")
        print(f"{place_to_stay} - {spend_money:.2f}")
    elif season == "winter":
        spend_money = budget * 0.7
        place_to_stay = "Hotel"
        print(f"Somewhere in {destination}")
        print(f"{place_to_stay} - {spend_money:.2f}")
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spend_money = budget * 0.4
        place_to_stay = "Camp"
        print(f"Somewhere in {destination}")
        print(f"{place_to_stay} - {spend_money:.2f}")
    elif season == "winter":
        spend_money = budget * 0.8
        place_to_stay = "Hotel"
        print(f"Somewhere in {destination}")
        print(f"{place_to_stay} - {spend_money:.2f}")
elif budget > 1000:
    destination = "Europe"
    spend_money = budget * 0.9
    place_to_stay = "Hotel"
    print(f"Somewhere in {destination}")
    print(f"{place_to_stay} - {spend_money:.2f}")


