import re

data = input()
pattern = r"([0-9]{2})([/.-]?)([A-Z][a-z]{2})\2([0-9]{4})\b"

for match in re.finditer(pattern, data):
    print(f"Day: {match.group(1)}, Month: {match.group(3)}, Year: {match.group(4)}")