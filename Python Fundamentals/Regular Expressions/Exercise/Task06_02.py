import re

pattern = r"www\.[A-Za-z0-9\-]+\.[a-z]+((\.[a-z]+)?)+"
data = input()

while data:

    matches = re.finditer(pattern, data)

    for match in matches:
        print(match.group(0))

    data = input()
