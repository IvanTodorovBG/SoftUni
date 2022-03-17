import re

data = input()
pattern = r">>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"
total_money = 0
furniture = []

while data != "Purchase":

    for match in re.finditer(pattern, data):
        total_money += float(match.group(2)) * float(match.group(4))
        furniture.append(match.group(1))

    data = input()

print("Bought furniture:")

for item in furniture:
    print(item)

print(f"Total money spend: {total_money:.2f}")
