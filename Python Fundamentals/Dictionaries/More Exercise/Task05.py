number_of_dragons = int(input())
dragons_dict = {}
for index in range(number_of_dragons):
    data = input().split()
    type = data[0]
    name = data[1]
    damage = data[2]
    health = data[3]
    armor = data[4]
    if damage == 'null':
        damage = 45
    damage = int(damage)
    if health == 'null':
        health = 250
    health = int(health)
    if armor == 'null':
        armor = 10
    armor = int(armor)
    if type not in dragons_dict:
        dragons_dict[type] = {}
        dragons_dict[type][name] = {'damage': damage, 'health': health, 'armor': armor}
    elif type in dragons_dict and name in dragons_dict[type]:
        dragons_dict[type][name]['damage'] = damage
        dragons_dict[type][name]['health'] = health
        dragons_dict[type][name]['armor'] = armor
    elif type in dragons_dict and name not in dragons_dict[type]:
        dragons_dict[type][name] = {'damage': damage, 'health': health, 'armor': armor}
# but dragons are sorted alphabetically by their name
# average damage, health, and armor of the dragons
for type, value in dragons_dict.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    sorted_dragons = dict(sorted(value.items(), key=lambda kvp: kvp[0]))
    for name, values in sorted_dragons.items():
        total_damage += values['damage']
        total_health += values['health']
        total_armor += values['armor']
    average_damage = total_damage / len(value)
    average_health = total_health / len(value)
    average_armor = total_armor / len(value)
    print(f"{type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for name, values in sorted_dragons.items():
        print(f"-{name} -> damage: {values['damage']}, health: {values['health']}, armor: {values['armor']}")