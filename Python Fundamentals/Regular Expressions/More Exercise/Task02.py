import re

data = input()
total_price = 0
pattern = r"%(?P<name>[A-Z][a-z]+)%([^\|$%.]+)?<(?P<product>\w+)>([^\|$%.]+)?\|(?P<count>[0-9]+)\|.*?(?P<price>(\d+\.?\d+))\$"
while data != "end of shift":

    matches = re.finditer(pattern, data)
    if matches:
        for match in matches:
            my_dict = match.groupdict()
            price = float(my_dict['price']) * int(my_dict['count'])
            total_price += price
            print(f"{my_dict['name']}: {my_dict['product']} - {price:.2f}")

    data = input()

print(f"Total income: {total_price:.2f}")
