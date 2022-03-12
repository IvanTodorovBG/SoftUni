import re

data = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

numbers = re.finditer(pattern, data)
for num in numbers:
    print(num[0], end=" ")
