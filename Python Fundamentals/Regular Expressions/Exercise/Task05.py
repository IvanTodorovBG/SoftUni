import re

data = input()
pattern = r"^>>(?P<furniture_name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)$"
furniture = []
total_money = 0
while data != "Purchase":

    for el in re.finditer(pattern, data):
        my_dict = el.groupdict()
        furniture.append(my_dict['furniture_name'])
        total_money += float(my_dict['price']) * int(my_dict['quantity'])
    data = input()

print("Bought furniture:")
for items in furniture:
    print(items)
print(f"Total money spend: {total_money:.2f}")