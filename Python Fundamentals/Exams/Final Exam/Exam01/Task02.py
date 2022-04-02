import re

data = input()
pattern = r"(\#|\|)(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1"
total_calories = 0
survive = {'item': [], 'date': [], 'calories': []}
matches = re.finditer(pattern, data)
for match in matches:
    my_dict = match.groupdict()
    total_calories += int(my_dict['calories'])

print(f"You have food to last you for: {int(total_calories/2000)} days!")

for match in re.finditer(pattern, data):
    my_dict = match.groupdict()
    print(f"Item: {my_dict['item']}, Best before: {my_dict['date']}, Nutrition: {my_dict['calories']}")

