import re

data = input()
pattern = r"(?P<day>[0-9]{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>[0-9]{4})"
matches = re.finditer(pattern, data)
for match in matches:
    d = match.groupdict()
    print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")