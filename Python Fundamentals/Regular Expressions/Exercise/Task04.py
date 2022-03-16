import re

data = input()
pattern = r"(^|(?<=\s))[a-z0-9]+([\._-][a-z0-9]+)?@[a-z]+([-][a-z]+)?\.[a-z]+([-][a-z]+)?(\.[a-z]+([-][a-z]+)?)?"
matches = re.finditer(pattern, data)
print('\n'.join([m.group(0) for m in matches]))
