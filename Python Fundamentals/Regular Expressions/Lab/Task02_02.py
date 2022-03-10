import re

data = input()
pattern = r"(^|(?<=\s))(\+359)(?P<separator>[\s\-])(2)(?P=separator)(\d{3})(?P=separator)(\d{4})\b"
phones = re.finditer(pattern, data)
phones = [p.group(0) for p in phones]
print(", ".join(phones))
