degrees = int(input())
day = input()

Outfit = ""
Shoes = ""

if 10 <= degrees <= 18:
    if day == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif day == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
if 18 < degrees <= 24:
    if day == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif day == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
if degrees >= 25:
    if day == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif day == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    elif day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

print(f"It\'s {degrees} degrees, get your {Outfit} and {Shoes}.")