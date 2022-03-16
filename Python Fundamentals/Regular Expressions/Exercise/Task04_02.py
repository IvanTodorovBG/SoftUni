import re

data = input()
pattern = r"(^|(?<=\s))([a-zA-Z0-9]+([\_.-][a-zA-Z0-9]+)?)@([a-zA-Z]+([\-][a-zA-Z]+)?)\.([a-zA-Z]+([\-][a-zA-Z]+)?)(\.([a-zA-Z]+([\-][a-zA-Z]+)?))*"

for match in re.finditer(pattern, data):
    print(match.group(0))
