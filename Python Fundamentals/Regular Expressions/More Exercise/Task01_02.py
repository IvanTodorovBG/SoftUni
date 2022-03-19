import re

players = input().split(", ")
data = input()
name_pattern = r"[a-zA-Z]"
number_pattern = r"\d"
winners = {}

while data != "end of race":
    current_name = []
    current_distance = 0
    for name in re.findall(name_pattern, data):
        current_name.append(name)
    current_name = "".join(current_name)
    if current_name in players:
        for km in re.findall(number_pattern, data):
            current_distance += int(km)
        if current_name not in winners:
            winners[current_name] = {}
            winners[current_name]['distance'] = 0
        winners[current_name]['distance'] += current_distance
    data = input()

sorted_winners = dict(sorted(winners.items(), key=lambda kvp: (-kvp[1]['distance'])))

winners_list = list(sorted_winners.keys())

print(f"""1st place: {winners_list[0]}
2nd place: {winners_list[1]}
3rd place: {winners_list[2]}""")