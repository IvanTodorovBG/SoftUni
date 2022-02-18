command = input()
counter = 0
new_dict = {}
key_list = []
value_list = []

while command != "stop":

    counter += 1
    if counter % 2 != 0:
        key_list.append(command)
    else:
        value_list.append(command)

    command = input()

new_list = list(zip(key_list, value_list))

for item in new_list:
    key = item[0]
    value = int(item[1])
    if key not in new_dict:
        new_dict[key] = value
    else:
        new_dict[key] += value

for key, value in new_dict.items():
    print(f"{key} -> {value}")
