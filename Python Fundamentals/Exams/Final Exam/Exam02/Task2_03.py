import re

data = input()
pattern = r"(\=|\/)([A-Z][a-zA-Z]{2,})\1"

print(f'Destinations: {", ".join([m.group(2) for m in re.finditer(pattern, data)])}')
print(f"Travel Points: {sum([len(i) for i in [m.group(2) for m in re.finditer(pattern, data)]])}")
