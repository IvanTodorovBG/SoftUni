import re

data = input()
pattern = r"\b(?P<web>www\.[a-zA-Z0-9]+([a-zA-Z0-9-]+)?\.[a-z]+((\.[a-z]+)?)+)"

while data:

    matches = re.finditer(pattern, data)

    for match in matches:
        my_dict = match.groupdict()
        print(my_dict['web'])

    data = input()
