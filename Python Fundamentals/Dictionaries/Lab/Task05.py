command = input().split(", ")
new_dict = {}

for key in command:
    if key not in new_dict:
        new_dict.setdefault(key, ord(key))

print(new_dict)
