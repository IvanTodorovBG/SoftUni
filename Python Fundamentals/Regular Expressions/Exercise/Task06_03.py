import re

data = input()
pattern = r"(www\.([a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*)\.([a-z]+(\.[a-z]+)*))"

while data != "":

    for match in re.finditer(pattern, data):
        print(match.group(1))

    data = input()
