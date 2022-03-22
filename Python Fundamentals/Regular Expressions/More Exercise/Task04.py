import re

info = input()

regex_letters = r'[^0-9+\-*\/\.]'
regex_numbers = r'[+|-]?\d+\.?\d*'
split = r"\s*,\s*|,\s*"
demon_split = sorted(re.split(split, info))
demons = {}

for demon in demon_split:
    # demon = demon.strip()
    letters = []
    numbers = []
    demons[demon] = []

    letters.append(re.findall(regex_letters, demon))
    numbers.append(re.findall(regex_numbers, demon))

    multiplies_count = demon.count("*")
    divides_count = demon.count("/")

    health = 0
    for letter in letters[0]:
        health += ord(letter)

    damage = 0
    for number in numbers[0]:
        damage += float(number)
    for i in range(0, multiplies_count):
        damage *= 2
    for i in range(0, divides_count):
        damage /= 2

    demons[demon].append(health)
    demons[demon].append(damage)

demons = dict(sorted(demons.items(), key=lambda x: x))

for demon in demons:
    print(f"{demon} - {demons[demon][0]} health, {demons[demon][1]:.2f} damage")