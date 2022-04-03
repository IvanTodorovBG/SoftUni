import re

data = input()
pattern = r"(\=|\/)([A-Z][a-zA-Z]{2,})\1"

matches = re.finditer(pattern, data)
destinations = list(m.group(2) for m in matches)
print(f'Destinations: {", ".join(destinations)}')
print(f"Travel Points: {sum([len(i) for i in destinations])}")
