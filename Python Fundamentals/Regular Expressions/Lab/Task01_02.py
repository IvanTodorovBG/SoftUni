import re

data = input()
pattern = r"\b([A-Z][a-z]+)\s([A-Z][a-z]+)\b"

matches = re.finditer(pattern, data)

for match in matches:
    print(match.group(), end=" ")
