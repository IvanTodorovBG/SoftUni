budget = float(input())
season = input()

location = ""
vacant_type = ""
price = 0

if budget <= 1000:
    vacant_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    vacant_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    else:
        location = "Morocco"
        price = budget * 0.6
elif budget > 3000:
    vacant_type = "Hotel"
    price = budget * 0.9
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} - {vacant_type} - {price:.2f}")