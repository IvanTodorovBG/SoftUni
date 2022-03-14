import re

data = input()
pattern = r"(^|(?<=\s))_(?P<name>[A-Za-z0-9]+)($|(?=\s))"
answer = []
for el in re.finditer(pattern, data):
    my_dict = el.groupdict()
    answer.append(my_dict['name'])

print(",".join(answer))
