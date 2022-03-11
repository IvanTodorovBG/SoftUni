import re

data = input()
pattern = r"\+359(\s|\-)?2\1[0-9]{3}\1[0-9]{4}\b"
matches = re.finditer(pattern, data)

print(", ".join(m.group() for m in re.finditer(pattern, data)))
