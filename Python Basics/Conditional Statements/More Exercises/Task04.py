distance = float(input())
day_or_nigh = input()

if distance < 20 and day_or_nigh == "day":
    money = 0.7 + (distance * 0.79)
    print(f"{money:.2f}")
elif distance < 20 and day_or_nigh == "night":
    money = 0.7 + (distance * 0.9)
    print(f"{money:.2f}")
elif 20 <= distance < 100:
    money = distance * 0.09
    print(f"{money:.2f}")
else:
    money = distance * 0.06
    print(f"{money:.2f}")