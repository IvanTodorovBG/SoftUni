countrys = input().split(", ")
cities = input().split(", ")

new_dict = dict(zip(countrys, cities))

for key in new_dict.items():
    print(f"{key[0]} -> {key[1]}")
