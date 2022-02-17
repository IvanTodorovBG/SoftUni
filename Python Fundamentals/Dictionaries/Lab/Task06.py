command = input().split(" ")
new_dict = {}
lower_list = []

for item in command:
    lower_list.append(item.lower())

for current_item in lower_list:
    if lower_list.count(current_item) % 2 != 0:
        new_dict[current_item] = lower_list.count(current_item)

print(" ".join(new_dict.keys()))
