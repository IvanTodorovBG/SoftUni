import re

data = input()
pattern = r"\b([0-9]{2})([-./])([A-Z][a-z]{2})\2([0-9]{4})\b"
matches = re.findall(pattern, data)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

