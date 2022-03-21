import re

n = int(input())

attacked = []
destroyed = []

for _ in range(n):
    data = input()
    pattern_count = r"(?i)[star]"
    count = len(re.findall(pattern_count, data))

    new_message = ""
    for letter in data:
        new_letter = chr(ord(letter) - count)
        new_message += new_letter

    pattern_planets = r'@(?P<planet>[a-zA-Z\s]+)([^\@:\!>-]+)?:(?P<population>\d+)([^\@:\!>-]+)?\!(?P<action>[A|D])\!([^\@:\!>-]+)?\->(?P<soldier>\d+)'
    matches = re.finditer(pattern_planets, new_message)
    if matches:
        for match in re.finditer(pattern_planets, new_message):
            planet_dict = match.groupdict()
            if planet_dict['action'] == 'A':
                attacked.append(planet_dict['planet'])
            if planet_dict['action'] == 'D':
                destroyed.append(planet_dict['planet'])

print(f"Attacked planets: {len(attacked)}")
if len(attacked) > 0:
    print("\n".join([f'-> {name}' for name in sorted(attacked)]))

print(f"Destroyed planets: {len(destroyed)}")
if len(destroyed) > 0:
    print("\n".join([f'-> {name}' for name in sorted(destroyed)]))