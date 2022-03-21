import re

data = input()
pattern = r"%([A-Z][a-z]+)%([^|$%.]+)?<(\w+)>([^|$%.]+)?\|(\d+)\|([^|$%.0-9]+)?([0-9]+(\.[0-9]+)?)\$"
total_income = 0

while data != "end of shift":

    for match in re.finditer(pattern, data):
        print(f"{match.group(1)}: {match.group(3)} - {int(match.group(5)) * float(match.group(7)):.2f}")
        total_income += int(match.group(5)) * float(match.group(7))
    data = input()

print(f"Total income: {total_income:.2f}")
