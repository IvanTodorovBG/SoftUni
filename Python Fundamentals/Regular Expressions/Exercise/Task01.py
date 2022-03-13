import re

data = input()
elements = []
pattern = r"\d+"

while data:

    elements.append(data)

    data = input()

for element in elements:
    numbers = re.findall(pattern, element)
    if numbers:
        print(" ".join(numbers), end=" ")
