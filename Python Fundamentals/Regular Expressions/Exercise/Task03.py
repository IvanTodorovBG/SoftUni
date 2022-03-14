import re
data = input().lower()
searched_word = input().lower()

patter = fr"\b{searched_word}\b"

matches = re.findall(patter, data)
print(len(matches))
