import re

data = input()
pattern = r"(\=|\/)([A-Z][a-zA-Z]{2,})\1"
travel_points = 0
destinations = []

for match in re.finditer(pattern, data):
    travel_points += len(match.group(2))
    destinations.append(match.group(2))

if destinations:
    print(f'Destinations: {", ".join(x for x in destinations)}')
    print(f"Travel Points: {travel_points}")
else:
    print("Destinations:")
    print("Travel Points: 0")
