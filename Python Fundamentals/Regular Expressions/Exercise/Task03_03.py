import re

data = input().lower()
search_word = input().lower()
pattern = fr"\b{search_word}\b"

print(len([match.group() for match in re.finditer(pattern, data)]))
